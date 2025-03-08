# import uiautomator2 as u2
# import cv2
# import numpy as np
# from io import BytesIO
# from PIL import Image

# def click_button_by_image(device_ip: str, template_path: str, threshold: float = 0.8) -> bool:
#     device = u2.connect(device_ip)
#     screenshot = device.screenshot()
#     image_bytes = BytesIO()
#     screenshot.save(image_bytes, format='PNG')
#     image_bytes.seek(0)
#     pil_image = Image.open(image_bytes)
#     screen_image = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)
#     template = cv2.imread(template_path, cv2.IMREAD_COLOR)
#     template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
#     screen_gray = cv2.cvtColor(screen_image, cv2.COLOR_BGR2GRAY)
#     result = cv2.matchTemplate(screen_gray, template_gray, cv2.TM_CCOEFF_NORMED)
#     min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

#     if max_val >= threshold:
#         h, w = template_gray.shape
#         center_x = max_loc[0] + w / 2
#         center_y = max_loc[1] + h / 2
#         print(f"Found button image at ({center_x}, {center_y}) with confidence {max_val:.2f}")

#         # Click vào vị trí trung tâm của button
#         device.click(center_x, center_y)
#         return max_loc, w, h
    
#     print(f"Không tìm thấy button với ngưỡng khớp {threshold}")
#     return False


# device_ip = 'R58NC2W4ZQK'  
# template_path = 'pic1.png' 
# click_button_by_image(device_ip, template_path, threshold=0.5)



import cv2
import numpy as np

def find_button_by_template(image, template, scales=[0.5, 0.75, 1.0, 1.25, 1.5], threshold=0.8):
    for scale in scales:
        resized_template = cv2.resize(template, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA)
        result = cv2.matchTemplate(image, resized_template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        if max_val >= threshold:
            print(f"Found template at scale {scale}")
            x, y = max_loc
            w, h = resized_template.shape[1], resized_template.shape[0]
            return x, y, w, h
    print("Template not found at any scale")
    return None

# Sử dụng function với các tỷ lệ khác nhau
image = cv2.imread('screenshot.png')
template = cv2.imread('pic1.png')
position = find_button_by_template(image, template)

if position:
    x, y, w, h = position
    print(f"Button found at: {x}, {y}, {w}x{h}")
else:
    print("Button not found")
