import QA_automation_phone as qa
from QA_automation_phone import u2
devices = qa.get_devices()
connect = u2.connect(devices[0])
x_screen, y_screen = qa.get_screen_size(devices[0])
x_screen = int(x_screen)
y_screen = int(y_screen)

# a= qa.scroll_find_element(device=devices[0],connect=connect,x_screen=x_screen, y_screen=y_screen,type_scroll="down", type_element="text",
#     value="Heart rate", duration=800, click=True)
# a= qa.scroll_find_element(device=devices[0],connect=connect,x_screen=x_screen, y_screen=y_screen,type_scroll="up", type_element="text",
#     value="Blood glucose", duration=800, click=True)
a= qa.scroll_up_and_down_find_element(device=devices[0],connect=connect,x_screen=x_screen, y_screen=y_screen, type_element="text",
    value="Heart rate", duration=600)
qa.click_element(device=devices[0],connect=connect, type_element="text", value="Heart rate", wait_time=2)

print(a)
