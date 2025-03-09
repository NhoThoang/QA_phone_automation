import uiautomator2 as u2
import pytesseract, time
from typing import Literal
language = Literal["eng", "vie"]
from QA_automation_phone.identify_image import screenshot
# def screenshot(connect: u2.connect):
#     screenshot = connect.screenshot()
#     image_bytes = BytesIO()
#     screenshot.save(image_bytes, format='PNG')
#     image_bytes.seek(0)
#     pil_image = Image.open(image_bytes)
#     image = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)
#     return image

def get_text_from_image(image, lang: language="eng") -> str:
    all_text = pytesseract.image_to_string(image, lang=lang)
    return all_text
def orc_click_button_by_text(connect: u2.connect, target_text: str, lang: language="eng", loop: int=1) -> bool:
    for _ in range(loop):
        image = screenshot(connect)
        text_data = pytesseract.image_to_data(image, lang=lang, output_type=pytesseract.Output.DICT)
        for i, text in enumerate(text_data['text']):
            if target_text.lower() in text.lower():
                x, y, w, h = (text_data['left'][i], text_data['top'][i], 
                            text_data['width'][i], text_data['height'][i])
                connect.click(x + w / 2, y + h / 2)
                return x, y, w, h
        time.sleep(0.5)
    print(f"Khong tim thay text: {target_text}")
    return False


