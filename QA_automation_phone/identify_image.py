import uiautomator2 as u2
import cv2
import numpy as np
from io import BytesIO
from PIL import Image
from QA_automation_phone.config import run_command, scroll_center_up_or_down, Literal, time, math
# def screenshot_to_cv2(connect: u2.connect):
#     screenshot = connect.screenshot()
#     image_bytes = BytesIO()
#     screenshot.save(image_bytes, format='PNG')
#     image_bytes.seek(0)
#     pil_image = Image.open(image_bytes)
#     image = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)
#     return image
def screenshot_to_cv2(connect: u2.connect):
    return cv2.cvtColor(np.array(connect.screenshot()), cv2.COLOR_RGB2BGR)

def get_crop_image(device: str, x1: int, y1: int, width: int, height: int, output_path: str="./template.png")->bool:
    command = f"adb -s {device} exec-out screencap -p"
    stauts = run_command(command=command)
    if stauts['returncode'] == 0:
        image = Image.open(BytesIO(stauts['stdout']))
        cropped_image = image.crop((x1, y1, x1 + width, y1 + height))
        cropped_image.save(output_path, format='PNG')
        return True
    else:
        return False
def are_images_identical(img1, img2):
    return np.array_equal(img1, img2)


def find_button_by_image(connect: u2.connect, template_path: str, threshold: float = 0.8,click: bool = False) -> bool:
    screenshot = connect.screenshot()
    image_bytes = BytesIO()
    screenshot.save(image_bytes, format='PNG')
    image_bytes.seek(0)
    pil_image = Image.open(image_bytes)
    screen_image = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)
    template = cv2.imread(template_path, cv2.IMREAD_COLOR)
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    screen_gray = cv2.cvtColor(screen_image, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(screen_gray, template_gray, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if max_val >= threshold:
        h, w = template_gray.shape
        center_x = max_loc[0] + w / 2
        center_y = max_loc[1] + h / 2
        if click:
            connect.click(center_x, center_y)
        return center_x, center_y, max_val
    print(f"threshold lớn nhất la: {max_val}<{threshold}")
    return False
def find_images_scroll_up_or_down(
    connect: u2.connect,
    device: str,
    x_screen: int,
    y_screen: int,
    template_path: str,
    scroll_type: Literal["up", "down"]="up",
    threshold: float = 0.8,
    duration: int=800,
    loop: int=2,
    max_loop: int=20)->bool:
    for _ in range(max_loop):
        data = find_button_by_image(connect=connect, template_path=template_path, threshold=threshold)
        if not data:
            if type == "up":
                if not scroll_center_up_or_down(device=device, x_screen=x_screen, y_screen=y_screen,type_scroll="up", duration=duration):
                    print(f"not scroll center up find {template_path}")
                    return False
            else:
                if not scroll_center_up_or_down(device=device, x_screen=x_screen, y_screen=y_screen,type_scroll="down", duration=duration):
                    print(f"not scroll center down find {template_path}")
                    return False
            time.sleep(0.5)
        else:
            return data
    print(f"not find {template_path} threshold lớn nhất la: {data[2]}<{threshold}")
    return False
def find_images_click_scroll_up_or_down_(connect: u2.connect,device: str,x_screen: int, y_screen: int, duration: int, type: Literal["up", "down"], template_path: str, threshold: float = 0.8, loop: int=2)->bool:
    data = find_images_scroll_up_or_down(connect=connect,device=device,x_screen=x_screen, y_screen=y_screen, duration=duration, type=type, template_path=template_path, threshold=threshold, loop=loop)
    if data:
        connect.click(data[0], data[1])
        return True
    print(f"not click {template_path} threshold lớn nhất la: {data[2]}<{threshold}")
    return False

# 

# scroll find image 
# scroll and click image