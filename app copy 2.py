# import uiautomator2 as u2

# device = 'R58NC2W4ZQK'  # Thay bằng ID thiết bị của bạn
# d = u2.connect(device)

# # Kiểm tra kết nối
# print(d.info)

# # Thử lấy text hoặc resource ID
# for element in d.xpath('//*').all():
#     print(element.attrib)
import uiautomator2 as u2

# Kết nối tới thiết bị qua device_id
device_id = 'R58NC2W4ZQK'
d = u2.connect(device_id)

# Dump toàn bộ UI hierarchy và lưu vào file XML
import time
start = time.time()
xml_data = d.dump_hierarchy()
print(time.time()-start)
# print(xml_data)

import xml.etree.ElementTree as ET


# Parse XML
tree = ET.fromstring(xml_data)

# Tìm tất cả các phần tử có resource-id cụ thể
value = "Settings"
type = "text"

elements = [elem for elem in tree.iter() if elem.attrib.get(type, "") == value]

if elements:
    bounds = elements[0].attrib.get('bounds', '')
    print(f"Bounds found: {bounds}")
else:
    print("Element not found!")

