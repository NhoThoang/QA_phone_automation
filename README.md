# UIAutomator2 Dump Screen Project

## Mục đích
Dự án này sử dụng `uiautomator2` để kết nối từ laptop tới server trên điện thoại Android, thực hiện dump màn hình và trả dữ liệu về laptop.
## Sơ đồ kết nối
![Sơ đồ kết nối](https://github.com/NhoThoang/QA_phone_automation/blob/main/picture/image1.png)

- **Laptop:** Gửi yêu cầu dump màn hình qua `uiautomator2`.
- **Điện thoại (Server UIAutomator2):** Nhận yêu cầu, thực hiện dump màn hình và gửi kết quả về laptop.

## Cài đặt
1. Cài đặt `qa_phone_automation` trên laptop:
```bash
pip install QA-automation-phone
```

2. Kết nối điện thoại với `qaautomation`:
```python
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
```

## Cách sử dụng
```python
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
```

## Lưu ý
- Điện thoại cần bật chế độ nhà phát triển và cấp quyền ADB.
- Đảm bảo `uiautomator2` server đang chạy trên điện thoại.
---
✅ **Nếu thấy hay và giúp ích cho các bạn bạn có thể gửi quà cho mình nhé Thanks!**

<img src="https://github.com/NhoThoang/QA_phone_automation/blob/main/picture/qr_pay.png" alt="QR Pay" width="100">

