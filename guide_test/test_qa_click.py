
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