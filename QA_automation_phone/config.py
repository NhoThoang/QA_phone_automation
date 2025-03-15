import subprocess
from typing import Literal
import uiautomator2 as u2
class config:
    def __init__(self, device: str = None, connect: u2.connect = None, x_screen: int = None, y_screen: int = None) -> None:
        self.device = device
        self.connect = connect
        self.x_screen = x_screen      
        self.y_screen = y_screen
    def run_command(self, command: str) -> dict:
        process = subprocess.Popen(
            command, 
            shell=True, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE
        )
        stdout, stderr = process.communicate()
        return {
            'stdout': stdout,
            'stderr': stderr,
            'returncode': process.returncode
        }
    def run_command_text(self, command: str) -> dict:
        process = subprocess.Popen(
            command, 
            shell=True, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE,
            text=True
        )
        stdout, stderr = process.communicate()
        return {
            'stdout': stdout.strip(),
            'stderr': stderr.strip(),
            'returncode': process.returncode
        }

    def adb_click(self, x:int, y:int)->bool:
        command = rf"adb -s {self.device} shell input tap {x} {y}"
        status = self.run_command(command=command)
        if status['returncode'] == 0:
            return True
        else:
            return False
    def adb_send(self, content: str)->bool:
        command = f"adb -s {self.device} shell input text '{content}'"
        status = self.run_command(command=command)
        if status['returncode'] == 0:
            return True
        else:
            return False
    def adb_click_send(self, x:int, y:int, content:str)->bool:
        if self.adb_click(x, y):
            if self.adb_send(content):
                return True
            else:
                return False
        else:
            return False
    def adb_keyevent(self, key: int)->bool:
        command = f"adb -s {self.device} shell input keyevent {key}"
        status = self.run_command(command=command)
        if status['returncode'] == 0:
            return True
        else:
            return False
    def scroll_height(self, x: int,y1: int, y2: int, duration: int=300)->bool:
        command = f"adb -s {self.device} shell input swipe {x} {y1} {x} {y2} {duration}"
        status = self.run_command(command=command)
        if status['returncode'] == 0:
            return True
        else:
            return False
    def scroll_width(self, x1: int, x2: int, y: int, duration: int=300)->bool:
        command = f"adb -s {self.device} shell input swipe {x1} {y} {x2} {y} {duration}"
        status = self.run_command(command=command)
        if status['returncode'] == 0:
            return True
        else:
            return False
    def scroll_up_or_down(self, x: int, y1: int, y2: int,type: Literal["up","down"]="up", duration: int=300)->bool:
        if type == "up":
            if self.scroll_height(x, y1, y2, duration):
                return True
            else:
                return False
        else:
            if self.scroll_height(x, y2, y1, duration):
                return True
            else:
                return False
    def scroll_left_or_right(self, x1: int, x2: int, y: int,type: Literal["left","right"]="left", duration: int=300)->bool:
        if type == "left":
            if self.scroll_width(x1, x2, y, duration):
                return True
            else:
                return False
        else:
            if self.scroll_width(x2, x1, y, duration):
                return True
            else:
                return False
    def scroll_top_or_bottom(self, type_scroll: Literal["up", "down"] = "up", duration: int=300)->bool:
        x= int(self.x_screen/2)
        y1 = int(self.y_screen*8/9)
        y2 = int(self.y_screen/10)
        if type_scroll == "up":
            if self.scroll_height(x, y1, y2, duration):
                return True
            else:
                return False
        else:
            if self.scroll_height(x, y2, y1, duration):
                return True
            else:
                return False

    def scroll_top_or_bottom_short(self, type_scroll: Literal["up", "down"] = "up",  duration: int=300)->bool:
        x= int(self.x_screen/2)
        y1 = int(self.y_screen/2)
        y2 = int(self.y_screen/9)
        if type_scroll == "up":
            if self.scroll_height(x, y1, y2, duration):
                return True
            else:
                return False
        else:
            if self.scroll_height(x, y2, y1, duration):
                return True
            else:
                return False

    def scroll_center_up_or_down(self, type_scroll: Literal["up", "down"] = "up",  duration: int=300)->bool:
        x= int(self.x_screen/2)
        y1 = int(self.y_screen/4)
        y2 = int(self.y_screen*3/4)
        if type_scroll == "up":
            if self.scroll_height(x, y2, y1, duration):
                return True
            else:
                return False
        else:
            if self.scroll_height(x, y1, y2, duration):
                return True
            else:
                return False
    def scroll_center_up_or_down_short(self, type_scroll: Literal["up", "down"] = "up",  duration: int=300)->bool:
        x= int(self.x_screen/2)
        y1 = int(self.y_screen/4)
        y2 = int(self.y_screen*3/5)
        if type_scroll == "up":
            if self.scroll_height(x, y2, y1, duration):
                return True
            else:
                return False
        else:
            if self.scroll_height(x, y1, y2, duration):
                return True
            else:
                return False
    def long_press(self, x: int, y: int, duration: int=1000)-> bool:
        command = f"adb -s {self.device} shell input swipe {x} {y} {x} {y} {duration}"
        status = self.run_command(command=command)
        if status['returncode'] == 0:
            return True
        else:
            return False

    def open_app(self, package)-> bool:
        command = f"adb -s {self.device} shell monkey -p {package} 1"
        status = self.run_command(command=command)
        if status['returncode'] == 0:
            return True
        else:
            return False


    def close_app(self, package: str)-> bool:
        command = f"adb -s {self.device} shell am force-stop {package}"
        status = self.run_command(command=command)
        if status['returncode'] == 0:
            return True
        else:
            return False

    def clear_cache(self)-> bool:
        command = f"adb -s {self.device} shell pm clear {self.device}"
        status = self.run_command(command=command)
        if status['returncode'] == 0:
            return True
        else:
            return False
 