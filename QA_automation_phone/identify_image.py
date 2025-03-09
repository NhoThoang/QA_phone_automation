import uiautomator2 as u2
import cv2
import numpy as np
from io import BytesIO
from PIL import Image
from QA_automation_phone.config import run_command
# from typing import Literal
def screenshot(connect: u2.connect):
    screenshot = connect.screenshot()
    image_bytes = BytesIO()
    screenshot.save(image_bytes, format='PNG')
    image_bytes.seek(0)
    pil_image = Image.open(image_bytes)
    image = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)
    return image
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
def click_button_by_image(device: str, template_path: str, threshold: float = 0.8) -> bool:
    device = u2.connect(device)
    screenshot = device.screenshot()
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
        # print(f"Found button image at ({center_x}, {center_y}) with confidence {max_val:.2f}")
        device.click(center_x, center_y)
        return center_x, center_y
    print(f"threshold lớn nhất la: {max_val}<{threshold}")
    return False
