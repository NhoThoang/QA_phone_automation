# from QA_automation_phone import u2
# import time
# import QA_automation_phone as qa

# from typing import Literal
# import threading
# devicess = qa.get_devices()
# device = devicess[0]
# screen_size = qa.get_screen_size(devicess[0])
# x_screen = int(screen_size[0])
# y_screen = int(screen_size[1])
# connect= u2.connect(devicess[0])

# time1 = time.time()
# qa.click_element(device=device, connect=connect, type="content-desc", value="Settings", wait_time=2)
# print("time to click by qa:", time.time() - time1)
# # time.sleep(2)
# # qa.press_back(device=device)
# # time.sleep(3)
# # time2 = time.time()
# # connect(text="Settings").click()
# # print("time to click by u2:", time.time() - time2)

# # time3 = time.time()
# # qa.screen_shot(device=device, output="screenshot.png")
# # print("time to screenshot by qa:", time.time() - time3)
# # time.sleep(3)
# # time4 = time.time()
# # connect.screenshot("screenshot.png")
# # print("time to screenshot by u2:", time.time() - time4)

# import uiautomator2 as u2

# # Kết nối tới thiết bị
# device = u2.connect('R58NC2W4ZQK')

# # Cuộn để tìm và click vào nút có text là "Samsung Health"
# device(scrollable=True).scroll.to(text="Blood pressure3")
# device(text="Blood pressure3").click()
import QA_automation_phone as qa
from QA_automation_phone import u2
devices = qa.get_devices()
connect = u2.connect(devices[0])
x_screen, y_screen = qa.get_screen_size(devices[0])
x_screen = int(x_screen)
y_screen = int(y_screen)
model = qa.get_model(devices)
print(model)
# qa.scroll_up_down_find_element_click(device=devices[0], x_screen=x_screen, y_screen=y_screen, connect=connect, type="text", value="Blood pressure", duration=500, loop=3)