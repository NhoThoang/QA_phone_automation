import uiautomator2 as u2
import pytesseract, time
from typing import Literal
from QA_automation_phone.identify_image import screenshot_to_cv2_gray, scroll_center_up_or_down, scroll_center_up_or_down_short, compare_images
import math
language = Literal["eng", "vie"]
def orc_get_text_from_image(connect: u2.connect, lang: language="eng") -> str:
    image = screenshot_to_cv2_gray(connect=connect)
    config = f'--oem 3 --psm 6 -l {lang}'
    all_text = pytesseract.image_to_string(image, config=config)
    return all_text

def orc_find_text_with_image(
    connect: u2.connect,
    target_text: str,
    screen_shot,
    index: int=0,
    lang: language="eng",
    click: bool=False) -> tuple:
    config = f'--oem 3 --psm 6 -l {lang}'
    text_data = pytesseract.image_to_data(screen_shot, config=config, output_type=pytesseract.Output.DICT)
    count = 0
    for i, text in enumerate(text_data['text']):
        if target_text.lower() in text.lower():
            count += 1
            if count == index + 1:
                x, y, w, h = (text_data['left'][i], text_data['top'][i], 
                                text_data['width'][i], text_data['height'][i])
                if click:
                    connect.click(x + w / 2, y + h / 2)
                screen_shot=None
                return x, y, w, h
    screen_shot=None
    return False
def orc_find_text(
    connect: u2.connect,
    target_text: str,
    index: int=0,
    lang: language="eng",
    wait_time: int=2,
    click: bool=False) -> tuple:
    loop = math.ceil(wait_time/2)
    for _ in range(loop):
        image = screenshot_to_cv2_gray(connect)
        config = f'--oem 3 --psm 6 -l {lang}'
        text_data = pytesseract.image_to_data(image, config=config, output_type=pytesseract.Output.DICT)
        count = 0
        for i, text in enumerate(text_data['text']):
            if target_text.lower() in text.lower():
                count += 1
                if count == index + 1:
                    x, y, w, h = (text_data['left'][i], text_data['top'][i], 
                                    text_data['width'][i], text_data['height'][i])
                    if click:
                        connect.click(x + w / 2, y + h / 2)
                    image=None
                    return x, y, w, h
        if loop > 1:
            time.sleep(0.5)
    return False


def orc_scroll_find_text(
    device: str,
    connect: u2.connect,
    target_text: str,
    x_screen: int, 
    y_screen: int, 
    index: int=0,
    lang: language="eng",
    type_scroll: Literal["up", "down"]="up",
    duration: int=800,
    click: bool=False,
    max_loop: int=20) -> tuple:
    screen_small = y_screen//4
    def fine_tune_scroll(y): 
        if y < screen_small or y > screen_small*3:
            print("fine tune scroll")
            if y < screen_small:
                scroll_center_up_or_down_short(device=device, x_screen=x_screen, y_screen=y_screen,type_scroll="down",duration=duration)
            if y > screen_small*3:
                scroll_center_up_or_down_short(device=device, x_screen=x_screen, y_screen=y_screen,type_scroll="up",duration=duration)
            time.sleep(1)
            return orc_find_text(connect=connect, target_text=target_text, index=index, lang=lang)    
        return False
    screen_short = screenshot_to_cv2_gray(connect=connect)
    loop = math.ceil(max_loop/2)
    for _ in range(loop):
        data= orc_find_text_with_image(connect=connect, target_text=target_text, screen_shot=screen_short,index=index,lang=lang)
        if data:
            y = data[1]
            data_fine_tune = fine_tune_scroll(y)
            if data_fine_tune:
                if click:
                    connect.click(data_fine_tune[0]+data_fine_tune[2]/2, data_fine_tune[1]+data_fine_tune[3]/2)
                return data_fine_tune
            if click:
                connect.click(data[0]+data[2]/2, data[1]+data[3]/2)
            return data
        if type_scroll == "up":
            scroll_center_up_or_down(device=device, x_screen=x_screen, y_screen=y_screen, type_scroll="up", duration=duration)                
        else:
            scroll_center_up_or_down(device=device, x_screen=x_screen, y_screen=y_screen, type_scroll="down", duration=duration)   
        time.sleep(1)
        new_screen = screenshot_to_cv2_gray(connect=connect)
        if compare_images(img1=screen_short, img2=new_screen):
            new_screen=None
            screen_short=None
            return False 
        screen_short = new_screen
    return False
def orc_scroll_up_and_dow_find_text(
    device: str,
    connect: u2.connect,
    target_text: str,
    x_screen: int, 
    y_screen: int, 
    index: int=0,
    lang: language="eng",
    duration: int=800,
    click: bool=False) -> tuple:
    data = orc_scroll_find_text(
        connect=connect,
        device=device,
        target_text=target_text,
        x_screen=x_screen,
        y_screen=y_screen,
        index=index,
        lang=lang,
        type_scroll="up",
        duration=duration,
        click=click)
    if data:
        return data
    data = orc_scroll_find_text(
        connect=connect,
        device=device,
        target_text=target_text,
        x_screen=x_screen,
        y_screen=y_screen,
        index=index,
        lang=lang,
        type_scroll="down",
        duration=duration,
        click=click)
    if data:
        return data
    return False
    
    
