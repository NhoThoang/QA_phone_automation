# README: UIAutomator2 Dump Screen Project

## Mục đích
Dự án này sử dụng `uiautomator2` để kết nối từ laptop tới server trên điện thoại Android, thực hiện dump màn hình và trả dữ liệu về laptop.
## Sơ đồ kết nối
![Sơ đồ kết nối](./picture/image1.png)

- **Laptop:** Gửi yêu cầu dump màn hình qua `uiautomator2`.
- **Điện thoại (Server UIAutomator2):** Nhận yêu cầu, thực hiện dump màn hình và gửi kết quả về laptop.

## Cài đặt
1. Cài đặt `qa_phone_automation` trên laptop:
```bash
pip install -U qaautomation
```

2. Kết nối điện thoại với `qaautomation`:
```python
import uiautomator2 as u2

device = u2.connect('device_ip')
print(device.info)
```

## Cách sử dụng
```python
from coreapp import get_xml_content

xml_data = get_xml_content('device_id', type='uiautomator')
print(xml_data)
```

## Lưu ý
- Điện thoại cần bật chế độ nhà phát triển và cấp quyền ADB.
- Đảm bảo `uiautomator2` server đang chạy trên điện thoại.

