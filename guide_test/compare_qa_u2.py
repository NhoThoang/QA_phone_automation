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

time1 = time.time()
qa.click_element(device=device, connect=connect, type="content-desc", value="Settings", wait_time=2)
print("time to click by qa:", time.time() - time1)
time.sleep(2)
qa.press_back(device=device)
time.sleep(3)
time2 = time.time()
connect(text="Settings").click()
print("time to click by u2:", time.time() - time2)

time3 = time.time()
qa.screen_shot(device=device, output="screenshot.png")
print("time to screenshot by qa:", time.time() - time3)
time.sleep(3)
time4 = time.time()
connect.screenshot("screenshot.png")
print("time to screenshot by u2:", time.time() - time4)