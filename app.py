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

# # Ví dụ sử dụng
# device_id = 'R58NC2W4ZQK'  # Thay bằng ID thiết bị thực tế
# import time
# start = time.time()
# click_button_home(device_id)
# print(time.time()-start)



from QA_automation_phone import coreapp, devices
from QA_automation_phone.coreapp import u2
import time
import threading
devicess = devices.get_devices()
def run(device_id):
    print("start")
    connect= u2.connect(device_id)
    start = time.time()
    if coreapp.click_element(device_id,connect, "text", "Settings", 0, 2):
        print("Clicked")
    else: 
        print("Not clicked")
    print(time.time()-start)

threads = []
for device in devicess:
    t = threading.Thread(target=run, args=(device,))
    threads.append(t)
for thread in threads:
    thread.start()