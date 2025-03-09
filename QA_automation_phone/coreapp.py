from QA_automation_phone.config import *
import time, math
# from QA_automation_phone.identify_image import screen_short_save_ram
ElementType = Literal["text", "content-desc", "resource-id"]
def get_xml_content(device: str)->str:
    command = f"adb -s {device} exec-out uiautomator dump /dev/stdout"
    result = run_command_text(command)
    if result['returncode'] == 0:
        return result['stdout'].replace('UI hierchary dumped to: /dev/stdout', "")  
    else:
        return result['stderr']
def get_xml_content_uiautomator2(connect)->str:
    if connect:
        return connect.dump_hierarchy()
    print("Not connected")
    return None

def wait_for_element(connect: u2.connect, value: str="", wait_time: int=2)->str:
    for _ in range(math.ceil(wait_time/2)):
        xml_content = get_xml_content_uiautomator2(connect)
        if xml_content:
            if value in xml_content:
                return xml_content
        time.sleep(0.5)
        # print(f"Waiting for element {type}: {value}...")
    return None
def wait_for_element_index(connect: u2.connect, value: str="",index: int=0, wait_time: int=2)->str:
    for _ in range(math.ceil(wait_time/2)):
        xml_content = get_xml_content_uiautomator2(connect)
        if xml_content:
            count = xml_content.count(value)
            if count > index:
                return xml_content
        time.sleep(0.5)
    return None
def get_bounds(connect: u2.connect, type: ElementType="text", value: str="", index: int=0, wait_time: int=2)->str:
    xml = wait_for_element(connect, value, wait_time)
    if xml:
        convert = ET.fromstring(xml)
        elements =  [element for element in convert.iter() if value in element.attrib.get(type,"")]
        if elements:
            return elements[index].attrib.get('bounds','')
    return None

def center_point_bounds(connect: u2.connect, type: ElementType="text", value: str="", index: int=0, wait_time: int=2)->tuple:
    bounds = get_bounds(connect, type, value, index, wait_time)
    if bounds:
        xy = eval(bounds.replace("][",","))
        return (xy[0]+xy[2])//2, (xy[1]+xy[3])//2
    return None
def click_element(device: str, connect: u2.connect, type: ElementType="text", value: str="", index: int=0, wait_time: int=2) -> tuple:
    xy = center_point_bounds(connect, type, value, index, wait_time)
    if xy:
        adb_click(device, xy[0], xy[1])
        return xy
    return None
def tab_and_send_text_to_element(device: str, type: ElementType="text", value: str="", index: int=0, wait_time: int=2, content: str="")-> tuple:
    xy = center_point_bounds(device, type, value, index, wait_time)
    if xy:
        adb_click_send(device, xy[0], xy[1],content)
        return xy
    return None


def get_bounds_all_element(connect: u2.connect, type: ElementType="text", value: str="", wait_time: int=2)->str:
    xml = wait_for_element(connect, type, value, wait_time)
    if xml:
        convert = ET.fromstring(xml)
        elements =  [element for element in convert.iter() if value in element.attrib.get(type,"")]
        if elements:
            return [element.attrib.get('bounds','') for element in elements]
        print(f"Not found element {type}: {value}")

def scroll_top_find_element_click(device: str, x_screen: int, y_screen: int, connect: u2.connect, type: ElementType="text", value: str="",index: int=0,duration: int=300, loop: int=2)->bool:
    for _ in range(loop):
        if click_element(device=device, connect=connect, type=type, value=value, index=index, wait_time=2):
            return True
        scroll_center_up(device=device, x_screen=x_screen, y_screen=y_screen, duration=duration)
        time.sleep(1)
    print(f"scroll top not found element {type}: {value} to click")
def scroll_bottom_find_element_click(device: str, x_screen: int, y_screen: int, connect: u2.connect, type: ElementType="text", value: str="",index: int=0, duration: int=300, loop: int=2)->bool:
    for _ in range(loop):
        if click_element(device=device, connect=connect, type=type, value=value, index=index, wait_time=2):
            return True
        scroll_center_down(device=device, x_screen=x_screen, y_screen=y_screen,duration=duration)
        time.sleep(1)
    print(f"scroll bottom not found element {type}: {value} to click")
def scroll_up_down_find_element_click(device: str, x_screen: int, y_screen: int, connect: u2.connect, type: ElementType="text", value: str="",index: int=0, duration: int=300, loop: int=2)->bool:
    if scroll_top_find_element_click(device=device, x_screen=x_screen, y_screen=y_screen, connect=connect, type=type, value=value, index=index,duration=duration, loop=loop):
        return True  
    time.sleep(1)
    if scroll_bottom_find_element_click(device=device, x_screen=x_screen, y_screen=y_screen, connect=connect, type=type, value=value, index=index,duration=duration, loop=loop):
        return True
    print(f"scroll up down not found element {type}: {value} to click")

def scroll_top_find_element(device: str, x_screen: int, y_screen: int, connect: u2.connect, type: ElementType="text", value: str="",duration: int=300, loop: int=2)->bool:
    for _ in range(loop):
        if wait_for_element(connect=connect, type=type, value=value, wait_time=2):
            return True
        scroll_center_up(device=device, x_screen=x_screen, y_screen=y_screen,duration=duration)
        time.sleep(1)
    print(f"scroll top not found element {type}: {value}")
def scroll_bottom_find_element(device: str, x_screen: int, y_screen: int, connect: u2.connect, type: ElementType="text", value: str="", duration: int=300, loop: int=2)->bool:
    for _ in range(loop):
        if wait_for_element(connect=connect, type=type, value=value, wait_time=2):
            return True
        scroll_center_down(device=device, x_screen=x_screen, y_screen=y_screen,duration=duration)
        time.sleep(1)
    print(f"scroll bottom not found element {type}: {value}")
def scroll_up_down_find_element(device: str, x_screen: int, y_screen: int, connect: u2.connect, type: ElementType="text", value: str="", duration: int=300, loop: int=2)->bool:
    if scroll_top_find_element(device=device, x_screen=x_screen, y_screen=y_screen, connect=connect, type=type, value=value,duration=duration, loop=loop):
        return True    
    if scroll_bottom_find_element(device=device, x_screen=x_screen, y_screen=y_screen, connect=connect, type=type, value=value,duration=duration, loop=loop):
        return True
    print(f"scroll up down not found element {type}: {value}")

# def get_image_crop(device: str, connect: u2.connect, type: ElementType="text", value: str="", index: int=0, wait_time: int=2, output_path: str="")->bool:
#     bounds = get_bounds(connect, type, value, index, wait_time)
#     print(bounds)
#     x1, y1, x2, y2 = eval(bounds.replace("][",","))
#     if screen_short_save_ram(device=device, output_path=output_path, x1=x1, x2=x2, y1=y1, y2=y2):
#         return True
#     else:
#         return False



def get_package(device: str)->str:
    command = f"adb -s {device} shell pm list packages"
    list_package = run_command_text(command=command)
    if list_package["returncode"] == 0:
        return list_package["stdout"]