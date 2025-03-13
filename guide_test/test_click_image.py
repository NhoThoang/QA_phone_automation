import QA_automation_phone as qa
import time
from QA_automation_phone import u2
devices = qa.get_devices()
connect = u2.connect(devices[0])
x_screen, y_screen = qa.get_screen_size(devices[0])
x_screen = int(x_screen)
y_screen = int(y_screen)
# qa.click_element(device=devices[0],connect=connect, value="Blood glucose")
# a= qa.get_crop_image_by_text(device=devices[0], connect=connect, value="Blood glucose",output_path="./picture1.png")
# a= qa.scroll_find_images(device=devices[0], connect=connect, x_screen=x_screen,y_screen=y_screen,
#                          template_path="./picture1.png",click=True)
# a= qa.scroll_up_and_dow_find_images(device=devices[0], connect=connect, x_screen=x_screen,y_screen=y_screen,
#     template_path="./picture1.png",click=True)
start = time.time()
a= qa.find_button_by_image(connect=connect, template_path="./picture1.png", threshold=0.8,click=True)
print(time.time()-start)
print(a)
