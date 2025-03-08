from QA_automation_phone.config import *

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

def wait_for_element(connect: u2.connect, type: Literal["text","content-desc", "resource-id"]="text", value: str="", loop: int=2)->str:
    for _ in range(loop):
        xml_content = get_xml_content_uiautomator2(connect)
        if xml_content:
            if type == "text":
                if value in xml_content:
                    return xml_content
            elif type == "content-desc":
                if value in xml_content:
                    return xml_content
            else:
                if value in xml_content:
                    return xml_content
    return None
def get_bounds(connect: u2.connect, type: Literal["text","content-desc", "resource-id"]="text", value: str="", index: int=0, loop: int=2)->str:
    xml = wait_for_element(connect, type, value, loop)
    if xml:
        convert = ET.fromstring(xml)
        elements =  [element for element in convert.iter() if value in element.attrib.get(type,"")]
        if elements:
            return elements[index].attrib.get('bounds','')
    return None

def center_point_bounds(connect: u2.connect, type: Literal["text","content-desc", "resource-id"]="text", value: str="", index: int=0, loop: int=2)->tuple:
    bounds = get_bounds(connect, type, value, index, loop)
    if bounds:
        xy = eval(bounds.replace("][",","))
        return (xy[0]+xy[2])//2, (xy[1]+xy[3])//2
    return None
def click_element(device: str, connect: u2.connect, type: Literal["text","content-desc", "resource-id"]="text", value: str="", index: int=0, loop: int=2):
    xy = center_point_bounds(connect, type, value, index, loop)
    if xy:
        adb_click(device, xy[0], xy[1])
        return xy
    return None
def tab_and_send_text_to_element(device: str, type: Literal["text","content-desc", "resource-id"], value: str, index: int=0, loop: int=2, content: str=""):
    xy = center_point_bounds(device, type, value, index, loop)
    if xy:
        adb_click_send(device, xy[0], xy[1],content)
        return xy
    return None


def get_bounds_all_element(connect: u2.connect, type: Literal["text","content-desc", "resource-id"]="text", value: str="", loop: int=2)->str:
    xml = wait_for_element(connect, type, value, loop)
    if xml:
        convert = ET.fromstring(xml)
        elements =  [element for element in convert.iter() if value in element.attrib.get(type,"")]
        if elements:
            return [element.attrib.get('bounds','') for element in elements]
        print(f"Not found element {type}: {value}")

def scroll_top_find_element(device: str, x_screen: int, y_screen: int, connect: u2.connect, type: Literal["text","content-desc", "resource-id"]="text", value: str="",index: int=0, loop: int=2)->str:
    for _ in range(loop):
        xml = wait_for_element(connect, type, value, loop)
        if xml:
            convert = ET.fromstring(xml)
            elements =  [element for element in convert.iter() if value in element.attrib.get(type,"")]
            if elements:
                return elements[index].attrib.get('bounds','')  
        scroll_top_short(device=device, x_screen=x_screen, y_screen=y_screen)
    print(f"Not found element {type}: {value}")
def scroll_bottom_find_element(device: str, x_screen: int, y_screen: int, connect: u2.connect, type: Literal["text","content-desc", "resource-id"]="text", value: str="",index: int=0, loop: int=2)->str:
    for _ in range(loop):
        xml = wait_for_element(connect, type, value, loop)
        if xml:
            convert = ET.fromstring(xml)
            elements =  [element for element in convert.iter() if value in element.attrib.get(type,"")]
            if elements:
                return elements[index].attrib.get('bounds','')  
        scroll_bottom_short(device=device, x_screen=x_screen, y_screen=y_screen)
    print(f"Not found element {type}: {value}")