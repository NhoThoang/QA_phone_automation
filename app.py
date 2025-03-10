# # import uiautomator2 as u2

# # def open_settings(device: str) -> bool:
# #     """
# #     Hàm mở ứng dụng Settings trên thiết bị Android.

# #     Args:
# #         device (str): ID của thiết bị Android (device serial).

# #     Returns:
# #         bool: True nếu mở thành công, False nếu gặp lỗi.
# #     """
# #     try:
# #         # Kết nối tới thiết bị
# #         d = u2.connect(device)
        
# #         # Kiểm tra kết nối bằng cách lấy thông tin thiết bị
# #         device_info = d.device_info
# #         if not device_info:
# #             print("Không thể kết nối tới thiết bị hoặc thiết bị không phản hồi.")
# #             return False
        
# #         # Quay về màn hình chính
# #         d.press("home")
        
# #         # Mở ứng dụng "Settings" thông qua package
# #         d.app_start("com.android.settings")

# #         # Kiểm tra xem đã vào "Settings" chưa
# #         if d(text="Settings").exists:
# #             print("Đã mở ứng dụng Settings thành công.")
# #             return True
# #         else:
# #             print("Không tìm thấy ứng dụng Settings.")
# #             return False

# #     except Exception as e:
# #         print(f"Lỗi khi mở ứng dụng Settings: {e}")
# #         return False

# # # Ví dụ sử dụng
# # device_id = 'R58NC2W4ZQK'  # Thay bằng ID thiết bị thực tế
# # open_settings(device_id)
# import uiautomator2 as u2

# def click_button_home(device: str) -> bool:
#     """
#     Hàm click vào button có text là "Home" trên thiết bị Android.

#     Args:
#         device (str): ID của thiết bị Android (device serial).

#     Returns:
#         bool: True nếu click thành công, False nếu gặp lỗi.
#     """
#     try:
#         # Kết nối tới thiết bị
#         d = u2.connect(device)
        
#         # Kiểm tra kết nối thiết bị
#         if not d.device_info:
#             print("Không thể kết nối tới thiết bị hoặc thiết bị không phản hồi.")
#             return False
        
#         # Kiểm tra và click vào button có text là "Home"
#         if d(text="Home").exists:
#             d(text="Home").click()
#             print("Đã click vào button 'Home' thành công.")
#             return True
#         else:
#             print("Không tìm thấy button 'Home'.")
#             return False

#     except Exception as e:
#         print(f"Lỗi khi click vào button 'Home': {e}")
#         return False

# # # Ví dụ sử dụng
# # device_id = 'R58NC2W4ZQK'  # Thay bằng ID thiết bị thực tế
# # import time
# # start = time.time()
# # click_button_home(device_id)
# # print(time.time()-start)



# from QA_automation_phone import coreapp, devices, identify_letter
# from QA_automation_phone.coreapp import u2
# import time
# import threading
# devicess = devices.get_devices()
# def run(device_id):
#     print("start")
#     connect= u2.connect(device_id)
#     start = time.time()
#     # if coreapp.click_element(device_id,connect, "text", "Settings", 0, 2):
#     if coreapp.click_element(device=device_id, connect=connect, type="content-desc", value="TikTok"):
#         print("Clicked")
#     else: 
#         print("Not clicked")
#     time.sleep(5)
#     # input("Press Enter to continue...")
#     if identify_letter.click_button_by_text(connect=connect, target_text="Profile", lang="eng", loop=5):
#         print("Clicked")
#     else:
#         print("Not clicked")
#     # if coreapp.click_element(device=device_id, connect=connect, type="content-desc", value="Profile"):
#     #     print("Clicked")
#     # else:
#     #     print("Not clicked")
#     print(time.time()-start)

# threads = []
# for device in devicess:
#     t = threading.Thread(target=run, args=(device,))
#     threads.append(t)
# for thread in threads:
#     thread.start()


from QA_automation_phone import u2
import time
import QA_automation_phone as qa

from typing import Literal
import threading
devicess = qa.get_devices()
device = devicess[0]
screen_size = qa.get_screen_size(devicess[0])
x_screen = int(screen_size[0])
y_screen = int(screen_size[1])
connect= u2.connect(devicess[0])
# (connect=connect, target_text="Profile", lang="eng", loop=5):
# text = qa.get_text_from_image(connect=connect, lang="vie")
# print(text)
start = time.time()
qa.orc_click_button_by_text(connect=connect, target_text="Samsung", lang="eng", loop=2, index=1)
print(time.time()-start)
# get template picture
# qa.get_crop_image(device=device, x1=795, y1=1564, width=200, height=300, output_path="./pic1.png")
# # click tempalte picture 
# qa.click_button_by_image(device=device, template_path="./pic1.png", threshold=0.8)

# device_ip = 'R58NC2W4ZQK'  
# template_path = 'pic1.png' 
# x,y = qa.click_button_by_image(device_ip, template_path, threshold=0.5)
# qa.adb_click(device_ip, x, y)

# def open_card_health(connect:u2.connect, device_id:str, x_screen: int, y_screen: int,type_device: Literal["slow", "medium", "fast"] = "phone",element_type: Literal["text", "content-desc", "resource-id"] = "text", element_value: str = ""):
#     if qa.scroll_up_down_find_element_click(device=device_id, x_screen=x_screen, y_screen=y_screen, connect=connect, type=element_type, value=element_value,duration=800, loop=3):
#         print(f"click card {element_value} ok")
#         if type_device == "slow":
#             time.sleep(5)
#             qa.press_back(device=device_id)
#         elif type_device == "medium":
#             time.sleep(3)
#             qa.press_back(device=device_id)
#         else:
#             time.sleep(2)
#             qa.press_back(device=device_id)

# def check_youtobe(connect:u2.connect, device_id:str):
#     qa.click_element(device=device_id, connect=connect, type="content-desc", value="Search")
#     time.sleep(2)
#     if qa.adb_send(device=device_id, content="Bac Bling"):
#         print("input done")
#     else:
#         print("input fail")
#     qa.press_enter(device=device_id)
#     time.sleep(2)

# def run(device_id, x_screen, y_screen,type_device):
#     print("start")
    
#     connect.send_keys("hello", clear=Truconnect= u2.connect(device_id)e)

#     if qa.open_app(device=device_id, package="com.sec.android.app.shealth"):
#         print("Opened")
#     else:
#         print("Not opened")
#     time.sleep(3)
#     # vuốt mạnh quá nên nó chôi đi dẫn đênc click vào rồi xong lại backra
#     open_card_health(connect=connect, device_id=device_id,x_screen=x_screen, y_screen=y_screen, type_device=type_device, element_type="content-desc", element_value="Steps")
#     time.sleep(2)
#     open_card_health(connect=connect, device_id=device_id,x_screen=x_screen, y_screen=y_screen, type_device=type_device, element_type="content-desc", element_value="Daily activity")
#     time.sleep(2)
#     open_card_health(connect=connect, device_id=device_id,x_screen=x_screen, y_screen=y_screen, type_device=type_device, element_type="content-desc", element_value="Sleep")
#     time.sleep(2)
#     open_card_health(connect=connect, device_id=device_id,x_screen=x_screen, y_screen=y_screen, type_device=type_device, element_type="content-desc", element_value="Food")
#     time.sleep(2)
#     open_card_health(connect=connect, device_id=device_id,x_screen=x_screen, y_screen=y_screen, type_device=type_device, element_type="content-desc", element_value="Water")
#     qa.close_app(device=device_id, package="com.sec.android.app.shealth")
#     time.sleep(3)
#     # open tiktok app
#     qa.open_app(device=device_id, package="	com.sec.android.app.launcher")
#     time.sleep(3)
#     check_youtobe(connect=connect, device_id=device_id)


    
#     # if coreapp.scroll_up_down_find_element_click(device=device_id, x_screen=x_screen, y_screen=y_screen, connect=connect, type="text", value="Water", loop=5):
#     #     print("Clicked")
#     # else:
#     #     print("Not clicked")
#     # time.sleep(5)
#     # if coreapp.close_app(device=device_id, package="com.sec.android.app.shealth"):
#     #     print("Closed")
#     # else:
#     #     print("Not closed")
#     # start = time.time()
#     # # if coreapp.click_element(device_id,connect, "text", "Settings", 0, 2):
#     # if coreapp.click_element(device=device_id, connect=connect, type="content-desc", value="TikTok"):
#     #     print("Clicked")
#     # else: 
#     #     print("Not clicked")
#     # time.sleep(5)
#     # # input("Press Enter to continue...")
#     # if identify_letter.click_button_by_text(connect=connect, target_text="Profile", lang="eng", loop=5):
#     #     print("Clicked")
#     # else:
#     #     print("Not clicked")
#     # # if coreapp.click_element(device=device_id, connect=connect, type="content-desc", value="Profile"):
#     # #     print("Clicked")
#     # # else:
#     # #     print("Not clicked")
#     # print(time.time()-start)

# threads = []
# for device in devicess:
#     t = threading.Thread(target=run, args=(device,x_screen,y_screen,"slow"))
#     threads.append(t)
# for thread in threads:
#     thread.start()


# # def abc():
# #     pass  # Hàm không return gì cả

# # if abc():
# #     print("Hàm trả về giá trị hợp lệ")
# # else:
# #     print("Hàm không trả về giá trị hoặc trả về giá trị 'falsy'")
