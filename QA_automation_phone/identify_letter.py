import uiautomator2 as u2
import pytesseract
import cv2
import numpy as np
from io import BytesIO
from PIL import Image
def screenshot(connect: u2.connect):
    screenshot = connect.screenshot()
    image_bytes = BytesIO()
    screenshot.save(image_bytes, format='PNG')
    image_bytes.seek(0)
    pil_image = Image.open(image_bytes)
    image = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)
    return image

def get_text_from_image(image, lang: str='eng') -> str:
    all_text = pytesseract.image_to_string(image, lang=lang)
    return all_text
def click_button_by_text(connect: u2.connect, target_text: str, lang: str='eng') -> bool:
    image = screenshot(connect)
    text_data = pytesseract.image_to_data(image, lang=lang, output_type=pytesseract.Output.DICT)
    for i, text in enumerate(text_data['text']):
        if target_text.lower() in text.lower():
            x, y, w, h = (text_data['left'][i], text_data['top'][i], 
                          text_data['width'][i], text_data['height'][i])
            connect.click(x + w / 2, y + h / 2)
            return x, y, w, h
    return False




device_ip = 'R58NC2W4ZQK'
connect = u2.connect(device_ip)
image = screenshot(connect)
  # Thay bằng IP thiết bị Android
target_text = 'Settings'    # Thay bằng văn bản trên button
import time
start = time.time()
text = get_text_from_image(image, 'eng')
print(text)
if click_button_by_text(image, target_text):
    print("Clicked")
else:
    print("Not clicked")
print(time.time()-start)
