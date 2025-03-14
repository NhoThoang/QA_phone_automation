
from QA_automation_phone import u2
import time
import QA_automation_phone as qa

from typing import Literal
import threading
devicess = qa.get_devices()
screen_size = qa.get_screen_size(devicess[0])
x_screen = int(screen_size[0])
y_screen = int(screen_size[1])
def open_card_health(connect:u2.connect, device_id:str, x_screen: int, y_screen: int, index: int = 0, type_element: str="content-desc", value: str=""):
    if not qa.wait_for_element(connect=connect, value="Home", wait_time=2):
        qa.open_app(device=device_id, package="com.sec.android.app.shealth")
        time.sleep(2)
    a = qa.scroll_up_and_down_find_element(connect=connect,device=device_id, x_screen=x_screen, y_screen=y_screen, value=value, type_element=type_element,index=index, duration=800, click=True)
    if a:
        # print(f"click done{a}")
        time.sleep(2)
        qa.press_back(device=device_id)
        return True

def check_youtobe(connect:u2.connect, device_id:str):
    qa.click_element(device=device_id, connect=connect, type_element="content-desc", value="Search")
    time.sleep(2)
    if qa.adb_send(device=device_id, content="Bac Bling"):
        print("input done")
    else:
        print("input fail")
    qa.press_enter(device=device_id)
    time.sleep(2)

def run(device_id, x_screen, y_screen):
    print("start")
    connect = u2.connect(device_id)
    # connect.send_keys("hello", clear=Truconnect= u2.connect(device_id)e)

    if qa.open_app(device=device_id, package="com.sec.android.app.shealth"):
        print("Opened")
    # else:
    #     print("Not opened")
    # time.sleep(3)
    # vuốt mạnh quá nên nó chôi đi dẫn đênc click vào rồi xong lại backra
    open_card_health(connect=connect, device_id=device_id,x_screen=x_screen, y_screen=y_screen, value="Steps",index=1 )
    time.sleep(2)
    open_card_health(connect=connect, device_id=device_id,x_screen=x_screen, y_screen=y_screen,  value="Daily")
    time.sleep(2)
    open_card_health(connect=connect, device_id=device_id,x_screen=x_screen, y_screen=y_screen,value="Sleep")
    time.sleep(2)
    open_card_health(connect=connect, device_id=device_id,x_screen=x_screen, y_screen=y_screen, value="Food")
    time.sleep(2)
    open_card_health(connect=connect, device_id=device_id,x_screen=x_screen, y_screen=y_screen, value="Water")
    qa.close_app(device=device_id, package="com.sec.android.app.shealth")
    time.sleep(3)
    # open tiktok app
    qa.open_app(device=device_id, package="com.google.android.youtube")
    time.sleep(3)
    check_youtobe(connect=connect, device_id=device_id)
threads = []
for device_id in devicess:
    thread = threading.Thread(target=run, args=(device_id, x_screen, y_screen))
    threads.append(thread)
for thread in threads:
    thread.start()