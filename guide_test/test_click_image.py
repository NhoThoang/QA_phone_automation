import QA_automation_phone as qa
import time, threading
devices = qa.get_devices()

def run(device):
    connect = qa.connect(device=device)
    start = time.time()
    a= connect.find_button_by_image(template_path="./picture1.png", threshold=0.8,click=True)
    print(time.time()-start)
    print(a)
threads = []    
for device in devices:
    t = threading.Thread(target=run, args=(device,))
    threads.append(t)
for thread in threads:
    thread.start()


# import QA_automation_phone as qa
# import time, threading
# devices = qa.get_devices()
# connect = qa.connect(device=devices[0])
# connect.get_crop_image(x1=795, y1=1564, width=200, height=300, output_path="./picture1.png")

# # connect.click_element(value="Blood glucose")
# a= connect.get_crop_image_by_text(value="Blood glucose",output_path="./picture1.png")
# # a= connect.scroll_find_images(template_path="./picture1.png",click=True)
# a= connect.scroll_up_and_dow_find_images(template_path="./picture1.png",click=True)


import QA_automation_phone as qa
import time, threading
devices = qa.get_devices()
connect = qa.connect(device=devices[0])
connect.find_button_by_image(template_path="./picture1.png", threshold=0.8,click=True)
connect.scroll_find_images(template_path="./picture1.png",type_scroll="up",click=True)
connect.scroll_up_and_dow_find_images(template_path="./picture1.png",click=True)
