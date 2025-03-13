import uiautomator2 as u2
import pytesseract, time
from typing import Literal
from QA_automation_phone.identify_image import screenshot_to_cv2_gray, scroll_center_up_or_down, scroll_center_up_or_down_short
import math
language = Literal["eng", "vie"]
def orc_get_text_from_image(connect: u2.connect, lang: language="eng") -> str:
    image = screenshot_to_cv2_gray(connect=connect)
    config = f'--oem 3 --psm 6 -l {lang}'
    all_text = pytesseract.image_to_string(image, config=config)
    return all_text
def orc_find_text(connect: u2.connect,
    target_text: str,
    lang: language="eng",
    wait_time: int=2,
    click: bool=False) -> tuple:
    loop = math.ceil(wait_time/2)
    for _ in range(loop):
        image = screenshot_to_cv2_gray(connect)
        config = f'--oem 3 --psm 6 -l {lang}'
        text_data = pytesseract.image_to_data(image, config=config, output_type=pytesseract.Output.DICT)
        for i, text in enumerate(text_data['text']):
            if target_text.lower() in text.lower():
                x, y, w, h = (text_data['left'][i], text_data['top'][i], 
                            text_data['width'][i], text_data['height'][i])
                if click:
                    connect.click(x + w / 2, y + h / 2)
                image=None
                return x, y, w, h
        if loop > 1:
            time.sleep(0.5)
    image=None
    return False
def orc_find_text(connect: u2.connect,
    target_text: str,
    lang: language="eng",
    wait_time: int=2,
    click: bool=False) -> tuple:
    loop = math.ceil(wait_time/2)
    for _ in range(loop):
        image = screenshot_to_cv2_gray(connect)
        config = f'--oem 3 --psm 6 -l {lang}'
        text_data = pytesseract.image_to_data(image, config=config, output_type=pytesseract.Output.DICT)
        for i, text in enumerate(text_data['text']):
            if target_text.lower() in text.lower():
                x, y, w, h = (text_data['left'][i], text_data['top'][i], 
                            text_data['width'][i], text_data['height'][i])
                if click:
                    connect.click(x + w / 2, y + h / 2)
                image=None
                return x, y, w, h
        if loop > 1:
            time.sleep(0.5)
    image=None
    return False
def orc_find_text_with_index(
    connect: u2.connect,
    target_text: str,
    lang: language="eng",
    loop: int=1,
    index: int=0,
    click: bool=False) -> tuple:
    for _ in range(loop):
        image = screenshot_to_cv2_gray(connect)
        config = f'--oem 3 --psm 6 -l {lang}'
        text_data = pytesseract.image_to_data(image, config=config, output_type=pytesseract.Output.DICT)
        matched_indices = []
        for i, text in enumerate(text_data['text']):
            if target_text.lower() in text.lower():
                matched_indices.append(i)
        if matched_indices and index < len(matched_indices):
            i = matched_indices[index] 
            x, y, w, h = (text_data['left'][i], text_data['top'][i], 
                          text_data['width'][i], text_data['height'][i])
            if click:
                connect.click(x + w / 2, y + h / 2)
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
    lang: language="eng",
    type_scroll: Literal["up", "down"]="up",
    loop: int=1,
    duration: int=500,
    click: bool=False) -> tuple:
    screen_small = y_screen//4
    def fine_tune_scroll(y): 
        if y < screen_small or y > screen_small*3:
            print("fine tune scroll")
            if y < screen_small:
                scroll_center_up_or_down_short(device=device, x_screen=x_screen, y_screen=y_screen,type_scroll="down",duration=duration)
            if y > screen_small*3:
                scroll_center_up_or_down_short(device=device, x_screen=x_screen, y_screen=y_screen,type_scroll="up",duration=duration)
            time.sleep(1)
            return orc_find_text(connect=connect, target_text=target_text, lang=lang)    
        return False
    for _ in range(loop):
        data= orc_find_text(connect=connect, target_text=target_text, lang=lang)
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
            scroll_center_up_or_down(connect=connect, x_screen=data[0], y_screen=data[1],type_scroll="up", duration=duration)   
            time.sleep(1)
            new_data = orc_find_text(connect=connect, target_text=target_text, lang=lang)
            if new_data:
        else:
            if data:
                if click:
                    connect.click(data[0]+data[2]/2, data[1]+data[3]/2)
                return data
            else:
                scroll_center_up_or_down(connect=connect, x_screen=data[0], y_screen=data[1],type_scroll="down", duration=duration)   
                time.sleep(1)
    return False




def orc_scroll_up_or_down_find_text_with_index(connect: u2.connect,device: str,x_screen: int, y_screen: int,duration: \
                                               int=500,type_scroll: Literal["up", "down"]="up", target_text: str="",\
                                                lang: language="eng", loop: int=1, index: int=0, click: bool=False) -> tuple:
    for _ in range(loop):
        data= orc_find_text_with_index(connect=connect, target_text=target_text, lang=lang, loop=1, index=index)
        if type_scroll == "up":
            if data:
                if click:
                    connect.click(data[0]+data[2]/2, data[1]+data[3]/2)
                return data
            else:
                scroll_center_up_or_down(device=device, x_screen=x_screen, y_screen=y_screen, duration=duration)
                time.sleep(1)
        else:
            if data:
                if click:
                    connect.click(data[0]+data[2]/2, data[1]+data[3]/2)
                return data
            else:
                scroll_center_up_or_down(device=device, x_screen=x_screen, y_screen=y_screen,type_scroll="down", duration=duration)
                time.sleep(1)
    return False


# import time
# import uiautomator2 as u2
# import pytesseract
# from typing import Tuple
# from pytesseract import Output

# def orc_click_button_by_text(connect: u2.Device, target_text: str, lang: str = "eng", loop: int = 1):
#     """
#     Tìm và click vào nút có chứa văn bản mục tiêu trên màn hình thiết bị Android.
    
#     Args:
#         connect (u2.Device): Đối tượng kết nối với thiết bị Android.
#         target_text (str): Văn bản cần tìm để nhấp chuột.
#         lang (str, optional): Ngôn ngữ nhận diện (mặc định là 'eng').
#         loop (int, optional): Số lần lặp lại nếu không tìm thấy (mặc định là 1).

#     Returns:
#         Tuple[int, int, int, int] or bool: Trả về tọa độ và kích thước vùng văn bản nếu thành công, False nếu thất bại.
#     """
#     for _ in range(loop):
#         image = screenshot_to_cv2(connect)
#         # Nhận diện văn bản trên toàn bộ ảnh với output là dạng từ điển
#         text_data = pytesseract.image_to_data(image, lang=lang, output_type=Output.DICT)
        
#         # Duyệt qua từng dòng thay vì từng từ riêng lẻ
#         for i, word in enumerate(text_data['text']):
#             if not word:
#                 continue
            
#             # Ghép nối các từ trên cùng một dòng lại với nhau
#             line_number = text_data['line_num'][i]
#             line_text = ' '.join(
#                 [text_data['text'][j] for j in range(len(text_data['text'])) 
#                  if text_data['line_num'][j] == line_number]
#             ).lower()
            
#             # Kiểm tra nếu chuỗi mục tiêu có trong chuỗi trên cùng một dòng
#             if target_text.lower() in line_text:
#                 x, y, w, h = (
#                     text_data['left'][i], 
#                     text_data['top'][i], 
#                     text_data['width'][i], 
#                     text_data['height'][i]
#                 )
#                 # Click vào trung tâm vùng chữ tìm được
#                 connect.click(x + w / 2, y + h / 2)
#                 print(f"Đã nhấp vào '{target_text}' tại vị trí ({x}, {y})")
#                 return x, y, w, h
        
#         # Nếu không tìm thấy, đợi và thử lại
#         time.sleep(0.5)
    
#     print(f"Không tìm thấy văn bản: {target_text}")
#     return False


# Ghép tối đa 5 từ liên tiếp
# def orc_click_button_by_text(connect: u2.connect, target_text: str, lang: str = "eng", loop: int = 1) -> bool:
#     for _ in range(loop):
#         image = screenshot_to_cv2(connect)
#         text_data = pytesseract.image_to_data(image, lang=lang, output_type=pytesseract.Output.DICT)
        
#         n_boxes = len(text_data['text'])
#         for i in range(n_boxes):
#             if not text_data['text'][i].strip():
#                 continue
            
#             # Tạo chuỗi ghép từ các ô lân cận để so sánh với target_text
#             combined_text = text_data['text'][i]
#             for j in range(i + 1, min(i + 5, n_boxes)):  # Ghép tối đa 5 từ liên tiếp
#                 if not text_data['text'][j].strip():
#                     continue
#                 combined_text += " " + text_data['text'][j]
                
#                 # Kiểm tra nếu chuỗi ghép khớp với target_text
#                 if target_text.lower() in combined_text.lower():
#                     x, y, w, h = (
#                         text_data['left'][i],
#                         text_data['top'][i],
#                         text_data['width'][i],
#                         text_data['height'][i]
#                     )
#                     connect.click(x + w / 2, y + h / 2)
#                     return x, y, w, h
        
#         time.sleep(0.5)
    
#     print(f"Không tìm thấy text: {target_text}")
#     return False

# Nếu giải pháp trên chưa đủ, có thể duyệt toàn bộ văn bản trên màn hình: 
# full_text = " ".join(text_data['text']).strip()
# print("Văn bản OCR:", full_text)

# if target_text.lower() in full_text.lower():
#     index = full_text.lower().index(target_text.lower())
#     # Tìm vị trí chính xác dựa trên chỉ số của từ đầu tiên
#     for i, text in enumerate(text_data['text']):
#         if text.lower().startswith(target_text.split()[0].lower()):
#             x, y, w, h = (text_data['left'][i], text_data['top'][i], 
#                           text_data['width'][i], text_data['height'][i])
#             connect.click(x + w / 2, y + h / 2)
#             return x, y, w, h


# khi cos space thi no se khogn click duoc fix no
# scroll fine text 
# scroll fine text click