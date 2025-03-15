import uiautomator2 as u2
import cv2, os
import numpy as np
from io import BytesIO
from PIL import Image
from QA_automation_phone.coreapp import coreapp,config, ElementType, math, time, Literal

class identify_image:
    def __init__(self,device: str = None, connect: u2.connect = None, x_screen: int = None, y_screen: int = None) -> None:
        self.coreapp = coreapp(device, connect, x_screen, y_screen)
        self.config = config(device, connect, x_screen, y_screen)
        self.device = device
        self.connect = connect
        self.x_screen = x_screen
        self.y_screen = y_screen
    def screenshot_to_cv2_color(self):
        return cv2.cvtColor(np.array(self.connect.screenshot()), cv2.COLOR_RGB2BGR)
    def screenshot_to_cv2_gray(self):
        return cv2.cvtColor(np.array(self.connect.screenshot()), cv2.COLOR_RGB2GRAY)
    def check_channel(self, image)->int:
        if len(image.shape) == 3:
            return 3
        else:
            return 1    
    def get_crop_image(self, x1: int, y1: int, width: int, height: int, output_path: str=None)->bool:
        command = f"adb -s {self.device} exec-out screencap -p"
        status = self.config.run_command(command=command)
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
        self,
        value: str="",
        output_path: str=None,
        type_element: ElementType="text",
        index: int=0,
        wait_time: int=2)->bool:
        bounds = self.coreapp.get_bounds(value, type_element, index, wait_time)
        if bounds:
            x1, y1, x2, y2 = eval(bounds.replace("][",","))
            width = x2-x1; height = y2-y1
            if self.get_crop_image(output_path=output_path, x1=x1, y1=y1, width=width, height=height):
                return True
            else:
                return False
        print(f"not find {value} type {type_element}")
        return False
    def compare_images(self, img1: np.ndarray, img2: np.ndarray)->bool:
        return np.array_equal(img1, img2)
    def find_button_by_image_with_image(
        self,
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
                self.connect.click(center_x, center_y)
            screen_short=None
            template_gray=None
            return center_x, center_y, max_val
        # print(f"Not found image {template_path} threshold lớn nhất la: {max_val}<{threshold}")
        screen_short=None
        template_gray=None
        return False  
    def find_button_by_image(self, template_path: str, threshold: float = 0.8, wait_time: int = 2, click: bool = False)->bool:
        loop = math.ceil(wait_time/2)
        for _ in range(loop):
            screen_gray = self.screenshot_to_cv2_gray()
            template_gray = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
            result = cv2.matchTemplate(screen_gray, template_gray, cv2.TM_CCOEFF_NORMED)
            _, max_val, _, max_loc = cv2.minMaxLoc(result)
            if max_val >= threshold:
                h, w = template_gray.shape
                center_x, center_y = max_loc[0] + w / 2, max_loc[1] + h / 2
                if click:
                    self.connect.click(center_x, center_y)
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
        self,
        template_path: str,
        threshold: float = 0.8,
        duration: int=800,
        type_scroll: Literal["up", "down"] = "up",
        max_loop: int=20,
        click: bool=False)->bool:
        screen_small = self.y_screen//4
        def fine_tune_scroll(y): 
            if y < screen_small or y > screen_small*3:
                if y < screen_small:
                    self.config.scroll_center_up_or_down_short(type_scroll="down",duration=duration)
                if y > screen_small*3:
                    self.config.scroll_center_up_or_down_short(type_scroll="up",duration=duration)
                time.sleep(1)
                return self.find_button_by_image(template_path=template_path, threshold=threshold)
            return False
        image_screen = self.screenshot_to_cv2_gray()
        # print(image_screen)
        for _ in range(max_loop):
            data = self.find_button_by_image_with_image(template_path=template_path, screen_short=image_screen, threshold=threshold)
            if data:
                x, y, max_val = data
                data_fine_tune = fine_tune_scroll(y)
                if data_fine_tune:
                    if click:
                        self.connect.click(data_fine_tune[0], data_fine_tune[1])
                    return data_fine_tune
                if click:
                    self.connect.click(x, y)
                return data
            if type_scroll == "up":
                self.config.scroll_center_up_or_down(type_scroll="up", duration=duration)
            else:
                self.config.scroll_center_up_or_down(type_scroll="down", duration=duration)
            time.sleep(1)
            new_image = self.screenshot_to_cv2_gray()
            if self.compare_images(img1=image_screen, img2=new_image):
                image_screen = None
                new_image = None
                return False   
            image_screen = new_image
        print(f"not find {template_path} threshold lớn nhất la: {data[2]}<{threshold}")
        return False

    def scroll_up_and_dow_find_images(
        self,
        template_path: str,
        threshold: float = 0.8,
        duration: int=800,
        max_loop: int=20,
        click: bool=False)->bool:
        data = self.scroll_find_images(
            template_path=template_path,
            threshold=threshold,
            duration=duration,
            type_scroll="up", 
            max_loop=max_loop,
            click=click)
        if data:
            return data
        data = self.scroll_find_images(
            template_path=template_path,
            threshold=threshold,
            duration=duration,
            type_scroll="down", 
            max_loop=max_loop,
            click=click)
        if data:
            return data
        return False