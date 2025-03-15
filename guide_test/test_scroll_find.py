import QA_automation_phone as qa
import time
devices = qa.get_devices()
cn = qa.connect(devices[0])

# a= cn.scroll_find_element(type_scroll="down", type_element="text", value="Heart rate", duration=800, click=True)
# a= cn.scroll_find_element(type_scroll="up", type_element="text", value="Blood glucose", duration=800, click=True)
# a= cn.scroll_up_and_down_find_element( type_element="text", value="Heart rate", duration=800)
# x,y=a
# time.sleep(3)
# cn.adb_click(x=x,y=y)
# import time
# time.sleep(2)
a= cn.click_element(type_element="text", value="Heart rate", wait_time=2)

print(a)