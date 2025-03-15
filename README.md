# Qa automation phone get screen by UI, screen short

## Mục đích
Dự án này kết nối từ laptop tới server trên điện thoại Android, thực hiện dump màn hình và trả dữ liệu về laptop hoặc lấy màn hình điện thoại về nhận diện   vị trí của text, button.
## Sơ đồ
```bash

                 ┌──────────────┐
                 │   Start      │
                 └──────┬───────┘
                        │
       ┌───────────────┴───────────────────┐
       │                                    │
  ┌────▼───────┐                     ┌────▼───────┐
  │ Dump UI    │                     │ Take       │
  │ to get     │                     │ Screenshot │
  │ button pos │                     └────┬──────┘
  └────┬───────┘                          │
       │                                  ▼
       ▼                        ┌─────────────────────┐
  ┌─────────┐                  │ Split into 2 paths  │
  │ Analyze │                  ├───────────┬────────┤
  │ UI      │                  │ Path 1    │ Path 2 │
  └────┬────┘                  ▼           ▼
       │                  ┌──────────┐  ┌──────────────┐
       ▼                  │ OCR       │  │ Image       │
  ┌──────────┐            │ detect    │  │ template    │
  │ Get      │            │ button    │  │ matching   │
  │ button   │            └────┬──────┘  └──────┬──────┘
  │ position │                 │               │
  └────┬─────┘                 ▼               ▼
       │                  ┌──────────┐    ┌──────────┐
       ▼                  │ Get       │    │ Get      │
  ┌───────────┐           │ button    │    │ button   │
  │ Compare   │           │ position  │    │ position │
  │ results   │           └────┬──────┘    └────┬──────┘
  └────┬──────┘                 │               │
       │                         ▼               ▼
  ┌──────────────────────┐   ┌──────────────┐  ┌──────────────┐
  │ Send command to      │   │ Send command │  │ Send command │
  │ button              │   │ to button    │  │ to button    │
  └─────────┬───────────┘   └────┬─────────┘  └────┬─────────┘
            ▼                     ▼                ▼
       ┌──────────┐           ┌───────────┐   ┌───────────┐
       │  End     │           │   End     │   │   End     │
       └──────────┘           └───────────┘   └───────────┘
```

- **Laptop:** Gửi yêu cầu dump màn hình qua điệnh thoại.
- **Điện thoại (Server trên điện thoại):** Nhận yêu cầu, thực hiện dump màn hình và gửi kết quả về laptop.
## code được viết dựa trên thư viện Uiautomator2 mình dùng function dump_hierarchy để lấy ui về xử lý 
các bạn có thể tha khảo link của thư viện U2 ở đây: ![link u2](https://github.com/openatx/uiautomator2)
## Cài đặt
1. Cài đặt `Qa-automation-phone` trên laptop:
```bash
pip install QA-automation-phone
```
## tiến hành chạy thử trên phone
### test tốc độ click trên model cũ 
#### để màn hình điện thoại có Button Settings để test
```python
import time
import QA_automation_phone as qa
connect = qa.connect()
start = time.time()
connect.connect(text="Settings").click()
print(time.time() - start)
```
### test tốc độ click trên model mới 
```python
import time
import QA_automation_phone as qa
connect = qa.connect()
start = time.time()
connect.click_element(value="Settings")
print(time.time() - start)
```
model mới được tối ưu hơn chạy nhanh hơn 1 chút 
## Lấy text, content cần chạy 1 server 
cần cài đặt 1 websever để lấy màn hình điện thoại 
```bash
pip install -U webitor
```
sau đó chạy ứng dụng 
```bash
python -m weditor
```
![giao diện weditor](https://github.com/NhoThoang/QA_phone_automation/blob/main/picture/weditor.png)

## Cách sử dụng chạy thử với đa luông 
```python

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
```
## Thao tác với orc
Hiện tại orc chỉ click vào được một từ đơn nếu giữa text có dấu cách thì sẽ không cick được.
VD:
```python
import QA_automation_phone as qa
devices = qa.get_devices()
cn = qa.connect(devices[0])
a= cn.orc_find_text(target_text="Samsung", lang="eng", index=1,click=True)
print(a)
```
code trên sẽ tìm chữ Samsung ở trên màn hình với lần xuất hiện là thứ 2 nếu target_text="Samsung Health" thì thư viện chưa hỗ trợ mình sẽ update sau 

❌ Code này sẽ không tìm được text là **Samsung Health**.
```python
import QA_automation_phone as qa
devices = qa.get_devices()
cn = qa.connect(devices[0])
a= cn.orc_find_text(target_text="Samsung Health", lang="eng", index=1,click=True)
print(a)
```
### các hàm hay dùng trong orc 
```python
import QA_automation_phone as qa
devices = qa.get_devices()
cn = qa.connect(devices[0])
a= cn.orc_find_text(target_text="Samsung", lang="eng", index=1,click=True)
cn.orc_find_text(target_text="Settings", lang="eng", index=1,click=True)
cn.orc_scroll_find_text(target_text="Heart rate", click=True)
cn.orc_scroll_up_and_dow_find_text(target_text="Heart rate", click=True)
print(a)
```

## Thao toác với ảnh:
để thao tác với ảnh các bạn cần có môt mẫu để so sánh thi viện của mình sẽ chuyển hết chúng về đen trắng để so sánh.
để lấy ảnh mẫy từ màn hình cách bạn chạy hàm dưới đây:
```python
import QA_automation_phone as qa
import time, threading
devices = qa.get_devices()
connect = qa.connect(device=devices[0])
connect.get_crop_image(x1=795, y1=1564, width=200, height=300, output_path="./picture1.png")
```
x, y là tọa độ điểm đầy phái trên bên trái của button   
width, height là độ rộng và cao của button   
sau khi chạy xong check ảnh picture1.png xem đúng chưa.
### tiến hành chạy thử nhận diện tìm kiếm vị trí của anh:
```python
import QA_automation_phone as qa
import time, threading
devices = qa.get_devices()
connect = qa.connect(device=devices[0])
connect.find_button_by_image(template_path="./picture1.png", threshold=0.8,click=True)
```
#### các hàm hay dùng trong tìm kiếm vị trí của ảnh để click:
```python
import QA_automation_phone as qa
import time, threading
devices = qa.get_devices()
connect = qa.connect(device=devices[0])
connect.find_button_by_image(template_path="./picture1.png", threshold=0.8,click=True)
connect.scroll_find_images(template_path="./picture1.png",type_scroll="up",click=True)
connect.scroll_up_and_dow_find_images(template_path="./picture1.png",click=True)
```
👉 **Nếu các bạn test có các issue quay lại video hay tạo issue trên repore này rồi gửi cho mình mình sex fix nhé !**
## Lưu ý:
- Điện thoại cần bật chế độ nhà phát triển và cấp quyền ADB.
- Đảm bảo server đang chạy trên điện thoại.
---
✅ **Nếu thấy hay và giúp ích cho các bạn bạn có thể gửi quà cho mình nhé Thanks!**

<img src="https://github.com/NhoThoang/QA_phone_automation/blob/main/picture/qr_pay.png" alt="QR Pay" width="100">

