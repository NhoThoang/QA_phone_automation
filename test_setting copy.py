import cv2

def crop_image(image_path, output_path, x, y, width, height):
    """
    Cắt một phần hình ảnh từ tọa độ (x, y) với kích thước (width, height).
    
    Args:
        image_path (str): Đường dẫn tới ảnh gốc.
        output_path (str): Đường dẫn để lưu ảnh đã cắt.
        x (int): Tọa độ x của góc trên trái vùng cần cắt.
        y (int): Tọa độ y của góc trên trái vùng cần cắt.
        width (int): Chiều rộng của vùng cần cắt.
        height (int): Chiều cao của vùng cần cắt.
        
    Returns:
        bool: Trả về True nếu cắt và lưu thành công, False nếu thất bại.
    """
    # Đọc ảnh gốc
    image = cv2.imread(image_path)
    
    if image is None:
        print(f"Không thể đọc ảnh từ {image_path}")
        return False
    
    # Kiểm tra vùng cắt có nằm trong ảnh gốc không
    img_height, img_width = image.shape[:2]
    if x < 0 or y < 0 or x + width > img_width or y + height > img_height:
        print("Vùng cắt nằm ngoài kích thước ảnh gốc!")
        return False
    
    # Cắt ảnh
    cropped_image = image[y:y+height, x:x+width]
    
    # Lưu ảnh đã cắt
    cv2.imwrite(output_path, cropped_image)
    print(f"Đã lưu ảnh cắt tại {output_path} với kích thước {width}x{height}")
    return True

# Ví dụ sử dụng:
crop_image(
    image_path='screenshot.png',
    output_path='pic1.png',
    x=795, y=1042, 
    width=246, height=368
)
