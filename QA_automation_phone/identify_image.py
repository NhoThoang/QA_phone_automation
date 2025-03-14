import uiautomator2 as u2
import cv2, os
import numpy as np
from io import BytesIO
from PIL import Image
from QA_automation_phone.coreapp import (get_bounds, ElementType, run_command, math, 
                                         scroll_center_up_or_down, scroll_center_up_or_down_short, Literal, time)

def screenshot_to_cv2_color(connect: u2.connect):
    return cv2.cvtColor(np.array(connect.screenshot()), cv2.COLOR_RGB2BGR)
def screenshot_to_cv2_gray(connect: u2.connect):
    return cv2.cvtColor(np.array(connect.screenshot()), cv2.COLOR_RGB2GRAY)
def check_channel(image)->int:
    if len(image.shape) == 3:
        return 3
    else:
        return 1    
def get_crop_image(device: str, x1: int, y1: int, width: int, height: int, output_path: str=None)->bool:
    command = f"adb -s {device} exec-out screencap -p"
    status = run_command(command=command)
    if status['returncode'] == 0:
        # image = Image.open(BytesIO(stauts['stdout']))
        with Image.open(BytesIO(status['stdout'])) as image:
            cropped_image = image.crop((x1, y1, x1 + width, y1 + height))
            if output_path:
                cropped_image.save(output_path, format='PNG')
            return cropped_image
    else:
        return False
def get_crop_image_by_text(
    device: str,
    connect: u2.connect,
    value: str="",
    output_path: str=None,
    type_element: ElementType="text",
    index: int=0,
    wait_time: int=2)->bool:
    bounds = get_bounds(connect, value, type_element, index, wait_time)
    if bounds:
        x1, y1, x2, y2 = eval(bounds.replace("][",","))
        width = x2-x1; height = y2-y1
        if get_crop_image(device=device, output_path=output_path, x1=x1, y1=y1, width=width, height=height):
            return True
        else:
            return False
    print(f"not find {value} type {type_element}")
    return False
def compare_images(img1: np.ndarray, img2: np.ndarray)->bool:
    return np.array_equal(img1, img2)
def find_button_by_image_with_image(
    connect: u2.connect,
    template_path: str,
    screen_short,
    threshold: float = 0.8,
    wait_time: int = 2,
    click: bool = False)->bool:
    if not os.path.exists(template_path):
        print("not find template and screen short")
        return False
    template_gray = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
    result = cv2.matchTemplate(screen_short, template_gray, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)
    if max_val >= threshold:
        h, w = template_gray.shape
        center_x, center_y = max_loc[0] + w / 2, max_loc[1] + h / 2
        if click:
            connect.click(center_x, center_y)
        screen_short=None
        template_gray=None
        return center_x, center_y, max_val
    # print(f"Not found image {template_path} threshold lớn nhất la: {max_val}<{threshold}")
    screen_short=None
    template_gray=None
    return False  
def find_button_by_image(connect: u2.connect, template_path: str, threshold: float = 0.8, wait_time: int = 2, click: bool = False)->bool:
    loop = math.ceil(wait_time/2)
    for _ in range(loop):
        screen_gray = screenshot_to_cv2_gray(connect=connect)
        template_gray = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
        result = cv2.matchTemplate(screen_gray, template_gray, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)
        if max_val >= threshold:
            h, w = template_gray.shape
            center_x, center_y = max_loc[0] + w / 2, max_loc[1] + h / 2
            if click:
                connect.click(center_x, center_y)
            screen_gray=None
            template_gray=None
            return center_x, center_y, max_val
        if loop > 1:
            time.sleep(0.5)
    print(f"Not found image {template_path} threshold lớn nhất la: {max_val}<{threshold}")
    screen_gray=None
    template_gray=None
    return False  
def scroll_find_images(
    device: str,
    connect: u2.connect,
    x_screen: int,
    y_screen: int,
    template_path: str,
    threshold: float = 0.8,
    duration: int=800,
    type_scroll: Literal["up", "down"] = "up",
    max_loop: int=20,
    click: bool=False)->bool:
    screen_small = y_screen//4
    def fine_tune_scroll(y): 
        if y < screen_small or y > screen_small*3:
            print("fine tune scroll")
            if y < screen_small:
                scroll_center_up_or_down_short(device=device, x_screen=x_screen, y_screen=y_screen,type_scroll="down",duration=duration)
            if y > screen_small*3:
                scroll_center_up_or_down_short(device=device, x_screen=x_screen, y_screen=y_screen,type_scroll="up",duration=duration)
            time.sleep(1)
            return find_button_by_image(connect=connect, template_path=template_path, threshold=threshold)
        return False
    image_screen = screenshot_to_cv2_gray(connect=connect)
    # print(image_screen)
    for _ in range(max_loop):
        data = find_button_by_image_with_image(connect=connect, template_path=template_path, screen_short=image_screen, threshold=threshold)
        if data:
            x, y, max_val = data
            data_fine_tune = fine_tune_scroll(y)
            if data_fine_tune:
                if click:
                    connect.click(data_fine_tune[0]+data_fine_tune[2]/2, data_fine_tune[1]+data_fine_tune[3]/2)
                return data_fine_tune
            if click:
                connect.click(x, y)
            return data
        if type_scroll == "up":
            scroll_center_up_or_down(device=device, x_screen=x_screen, y_screen=y_screen,type_scroll="up", duration=duration)
        else:
            scroll_center_up_or_down(device=device, x_screen=x_screen, y_screen=y_screen,type_scroll="down", duration=duration)
        time.sleep(1)
        new_image = screenshot_to_cv2_gray(connect=connect)
        if compare_images(img1=image_screen, img2=new_image):
            image_screen = None
            new_image = None
            return False   
        image_screen = new_image
    print(f"not find {template_path} threshold lớn nhất la: {data[2]}<{threshold}")
    return False

def scroll_up_and_dow_find_images(
    device: str,
    connect: u2.connect,
    x_screen: int,
    y_screen: int,
    template_path: str,
    threshold: float = 0.8,
    duration: int=800,
    max_loop: int=20,
    click: bool=False)->bool:
    data = scroll_find_images(
        connect=connect,
        device=device,
        x_screen=x_screen,
        y_screen=y_screen,
        template_path=template_path,
        threshold=threshold,
        duration=duration,
        type_scroll="up", 
        max_loop=max_loop,
        click=click)
    if data:
        return data
    data = scroll_find_images(
        connect=connect,
        device=device,
        x_screen=x_screen,
        y_screen=y_screen,
        template_path=template_path,
        threshold=threshold,
        duration=duration,
        type_scroll="down", 
        max_loop=max_loop,
        click=click)
    if data:
        return data
    return False