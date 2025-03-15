
import time
import QA_automation_phone as qa
import threading
devicess = qa.get_devices()

def open_card_health(connect, index: int = 0, type_element: str="content-desc", value: str=""):
    if not connect.wait_for_element(value="Home", wait_time=2):
        connect.open_app(package="com.sec.android.app.shealth")
        time.sleep(2)
    a = connect.scroll_up_and_down_find_element(value=value, type_element=type_element,index=index, duration=800, click=True)
    if a:
        time.sleep(2)
        if connect.wait_for_element(value=value, wait_time=2):
            time.sleep(2)
            connect.press_back()
            return True

def check_youtobe(connect):
    connect.click_element(type_element="content-desc", value="Search")
    time.sleep(2)
    if  connect.adb_send(content="Bac Bling"):
        print("input done")
    else:
        print("input fail")
    connect.press_enter()
    time.sleep(2)

def run(device_id):
    print("start")
    connect = qa.connect(device=device_id)

    if connect.open_app(package="com.sec.android.app.shealth"):
        print("Opened")

    open_card_health(connect=connect,value="Steps",index=1 )
    time.sleep(2)
    open_card_health(connect=connect,value="Daily")
    time.sleep(2)
    open_card_health(connect=connect,value="Sleep")
    time.sleep(2)
    open_card_health(connect=connect,value="Food")
    time.sleep(2)
    open_card_health(connect=connect,value="Water")
    connect.close_app(package="com.sec.android.app.shealth")
    time.sleep(3)
    # open tiktok app
    connect.open_app(package="com.google.android.youtube")
    time.sleep(3)
    check_youtobe(connect=connect)
threads = []
for device_id in devicess:
    thread = threading.Thread(target=run, args=(device_id,))
    threads.append(thread)
for thread in threads:
    thread.start()