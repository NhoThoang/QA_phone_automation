

import QA_automation_phone as qa
import time, threading  
devices = qa.get_devices()
def run(device):
    connect = qa.connect(device=device)
    start = time.time()
    if connect.click_element(value="Settings"):
        print("Clicked")
    else: 
        print("Not clicked")
    print(time.time()-start)

threads = []
for device in devices:
    t = threading.Thread(target=run, args=(device,))
    threads.append(t)
for thread in threads:
    thread.start()