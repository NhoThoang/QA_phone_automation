# from QA_automation_phone.config import (Literal, run_command_text, scroll_height, adb_click, adb_click_send,run_command,
#                                         scroll_center_up_or_down, scroll_top_or_bottom_short,scroll_center_up_or_down_short)
from QA_automation_phone.config import config, u2, Literal
import xml.etree.ElementTree as ET
import time, math
ElementType = Literal["text", "content-desc", "resource-id"]
class coreapp:
    def __init__(self,device: str = None, connect: u2.connect = None, x_screen: int = None, y_screen: int = None) -> None:
        self.config = config(device=device, connect=connect, x_screen=x_screen, y_screen=y_screen)
        self.device = device
        self.connect = connect
        self.x_screen = x_screen
        self.y_screen = y_screen
    def get_xml_content(self)->str:
        command = f"adb -s {self.device} exec-out uiautomator dump /dev/stdout"
        result = self.config.run_command_text(command)
        if result['returncode'] == 0:
            return result['stdout'].replace('UI hierchary dumped to: /dev/stdout', "")  
        else:
            return result['stderr']
    def get_xml_content_uiautomator2(self)->str:
        if self.connect:
            return self.connect.dump_hierarchy()
        print("Not connected")
        return None

    def wait_for_element(
        self,
        value: str="",
        wait_time: int=2)->str:
        loop = math.ceil(wait_time/2)
        for _ in range(loop):
            xml_content = self.get_xml_content_uiautomator2()
            if xml_content:
                if value in xml_content:
                    return xml_content
            if loop > 1:
                time.sleep(0.5)
        return None
    def wait_for_element_index(
        self,
        value: str="",
        index: int=0,
        wait_time: int=2)->str:
        loop = math.ceil(wait_time/2)
        for _ in range(loop):
            xml_content = self.get_xml_content_uiautomator2()
            if xml_content:
                count = xml_content.count(value)
                if count > index:
                    return xml_content
            if loop > 1:
                time.sleep(0.5)
        return None
    def get_bounds(
        self,
        value: str="",
        type_element: ElementType="text",
        index: int=0,
        wait_time: int=2)->str:
        xml = self.wait_for_element(value, wait_time)
        if xml:
            convert = ET.fromstring(xml)
            elements = [element for element in convert.iter() if value in element.attrib.get(type_element,"")]
            if elements:
                xml = None
                return elements[index].attrib.get('bounds','')
        xml = None
        return None
    def center_point_bounds(
        self,
        value: str = "",
        type_element: ElementType = "text",  
        index: int = 0, 
        wait_time: int = 2) -> tuple:
        bounds = self.get_bounds(value, type_element, index, wait_time)
        if bounds:
            xy = eval(bounds.replace("][",","))
            return (xy[0]+xy[2])//2, (xy[1]+xy[3])//2
        return None
    def center_point_bounds_with_xml(
        self,
        xml: str,
        value: str = "",
        type_element: ElementType = "text",  
        index: int = 0) -> tuple:
        if xml:
            convert = ET.fromstring(xml)
            elements = [element for element in convert.iter() if value in element.attrib.get(type_element,"")]
            if elements:
                bounds = elements[index].attrib.get('bounds','')
                xy = eval(bounds.replace("][",","))
                xml = None
                return (xy[0]+xy[2])//2, (xy[1]+xy[3])//2
        xml = None
        return None
    def click_element(
        self,
        value: str = "",
        type_element: ElementType = "text", 
        index: int = 0, 
        wait_time: int = 2) -> tuple:
        xy = self.center_point_bounds(value=value, type_element=type_element, index=index,wait_time=wait_time)
        if xy:
            self.config.adb_click(xy[0], xy[1])
            return xy
        return None
    def click_element_when_xml_contains(
        self,
        xml: str,
        device: str,  
        value: str = "", 
        type_element: ElementType = "text", 
        index: int = 0,) -> tuple:
        if xml:
            convert = ET.fromstring(xml)
            elements = [element for element in convert.iter() if value in element.attrib.get(type_element,"")]
            if elements:
                bounds = elements[index].attrib.get('bounds','')
                xy = eval(bounds.replace("][",","))
                x, y = (xy[0]+xy[2])//2, (xy[1]+xy[3])//2
                self.config.adb_click(device, x, y)
                xml = None
                return x, y
        xml = None
        return None
        
    def tab_and_send_text_to_element(
        self,
        value: str = "",
        type_element: ElementType = "text",  
        index: int = 0, 
        wait_time: int = 2, 
        content: str = "") -> tuple:
        xy = self.center_point_bounds(value, type_element, index, wait_time)
        if xy:
            self.config.adb_click_send(xy[0], xy[1],content)
            return xy
        return None

    def get_bounds_all_element(
        self,
        value: str = "",
        type_element: ElementType = "text", 
        wait_time: int = 2) -> str:
        xml = self.wait_for_element(value, wait_time)
        if xml:
            convert = ET.fromstring(xml)
            elements = [element for element in convert.iter() if value in element.attrib.get(type_element,"")]
            if elements:
                xml = None
                return [element.attrib.get('bounds','') for element in elements]
            print(f"Not found element {type_element}: {value}")
        xml = None
        return None

    def scroll_find_element(
        self, 
        value: str = "", 
        type_element: ElementType = "text",
        index: int = 0,
        duration: int = 800, 
        type_scroll: Literal["up", "down"] = "up", 
        max_loop: int = 20,
        click: bool = False) -> bool: 
        screen_small = self.y_screen//4
        def fine_tune_scroll(y): 
            if y < screen_small or y > screen_small*3:
                if y < screen_small:
                    self.config.scroll_center_up_or_down_short(type_scroll="down",duration=duration)
                if y > screen_small*3:
                    self.config.scroll_center_up_or_down_short(type_scroll="up",duration=duration)
                time.sleep(1)
                return self.center_point_bounds(value=value, type_element=type_element, index=index, wait_time=2)
            return False
        xml = self.get_xml_content_uiautomator2()
        for _ in range(max_loop):
            data = self.center_point_bounds_with_xml(xml=xml, value=value, type_element=type_element, index=index)
            if data:
                x,y = data
                data_fine_tune = fine_tune_scroll(y)
                if data_fine_tune:
                    if click:
                        self.config.adb_click(data_fine_tune[0], data_fine_tune[1])
                    xml = None
                    return data_fine_tune
                if click:
                    self.config.adb_click(x, y)
                xml = None
                return data
            if type_scroll == "up":
                self.config.scroll_center_up_or_down(type_scroll="up",duration=duration)
            else:
                self.config.scroll_center_up_or_down(type_scroll="down",duration=duration)
            time.sleep(1)
            new_xml = self.get_xml_content_uiautomator2()
            if new_xml == xml:
                xml = None; new_xml = None
                return False
            xml = new_xml
        return False

    def scroll_up_and_down_find_element(
        self,                       
        value: str="",
        type_element: ElementType = "text",
        index: int = 0,
        duration: int=800,
        click: bool = False)->tuple:
        data = self.scroll_find_element(
            value=value,
            type_element=type_element,
            index=index,
            duration=duration,
            type_scroll="up",
            click=click)
        if data:
            return data   
        data = self.scroll_find_element(
            value=value,
            type_element=type_element,
            index=index,
            duration=duration,
            type_scroll="down")
        if data:
            return data
        return False
    def get_package(self, device: str)->str:
        command = f"adb -s {device} shell pm list packages"
        list_package = self.config.run_command_text(command=command)
        if list_package["returncode"] == 0:
            return list_package["stdout"]    

    # def get_image_crop(device: str, connect: u2.connect, type: ElementType="text", value: str="", index: int=0, wait_time: int=2, output_path: str="")->bool:
    #     bounds = get_bounds(connect, type, value, index, wait_time)
    #     print(bounds)
    #     x1, y1, x2, y2 = eval(bounds.replace("][",","))
    #     if screenshort(device=device, output_path=output_path, x1=x1, x2=x2, y1=y1, y2=y2):
    #         return True
    #     else:
    #         return False
