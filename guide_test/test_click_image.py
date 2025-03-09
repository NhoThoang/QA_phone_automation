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
# get template picture
qa.get_crop_image(device=device, x1=795, y1=1564, width=200, height=300, output_path="./pic1.png")
# click tempalte picture 
qa.click_button_by_image(device=device, template_path="./pic1.png", threshold=0.8)
