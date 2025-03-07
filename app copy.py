import uiautomator2 as u2
from PIL import Image

def view_device_screen(device: str, save_path: str = "screenshot.png"):
    """
    Chụp màn hình thiết bị và hiển thị ảnh.

    Args:
        device (str): ID của thiết bị Android (device serial).
        save_path (str): Đường dẫn lưu ảnh chụp màn hình.
    """
    try:
        # Kết nối tới thiết bị
        d = u2.connect(device)

        # Chụp màn hình và lưu lại
        d.screenshot(save_path)
        print(f"Đã lưu ảnh chụp màn hình tại: {save_path}")
        
        # Hiển thị ảnh (yêu cầu thư viện Pillow - PIL)
        img = Image.open(save_path)
        img.show()

    except Exception as e:
        print(f"Lỗi khi chụp màn hình: {e}")

# Ví dụ sử dụng
device_id = 'R58NC2W4ZQK'  # Thay bằng ID thiết bị thực tế
view_device_screen(device_id)
