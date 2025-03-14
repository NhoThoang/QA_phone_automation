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

## Cài đặt
1. Cài đặt `Qa-automation-phone` trên laptop:
```bash
pip install QA-automation-phone
```
## tiến hành chạy thử để cài đặt server trên phone
```bash
import QA_automation_phone as qa
connect = qa.u2.connect()
print(connect.info)
```
## lấy text, content cần chạy 1 server 
```bash
python -m weditor
```
![giao diện weditor](https://github.com/NhoThoang/QA_phone_automation/blob/main/picture/weditor.png)

## Cách sử dụng chạy thử với đa luông 
```python
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

    if qa.open_app(device=device_id, package="com.sec.android.app.shealth"):
        print("Opened")

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
    thread.start()()
```

## Lưu ý
- Điện thoại cần bật chế độ nhà phát triển và cấp quyền ADB.
- Đảm bảo server đang chạy trên điện thoại.
---
✅ **Nếu thấy hay và giúp ích cho các bạn bạn có thể gửi quà cho mình nhé Thanks!**

<img src="https://github.com/NhoThoang/QA_phone_automation/blob/main/picture/qr_pay.png" alt="QR Pay" width="100">

