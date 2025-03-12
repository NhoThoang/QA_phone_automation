import subprocess
from typing import Literal
def run_command(command: str) -> dict:
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
def run_command_text(command: str) -> dict:
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

def adb_click(device: str,x:int,y:int)->bool:
    command = rf"adb -s {device} shell input tap {x} {y}"
    status = run_command(command=command)
    if status['returncode'] == 0:
        return True
    else:
        return False
def adb_send(device: str,content: str)->bool:
    command = f"adb -s {device} shell input text '{content}'"
    status = run_command(command=command)
    if status['returncode'] == 0:
        return True
    else:
        return False
def adb_click_send(device: str,x:int,y:int,content:str)->bool:
    if adb_click(device, x, y):
        if adb_send(device, content):
            return True
        else:
            return False
    else:
        return False
def adb_keyevent(device: str,key: int)->bool:
    command = f"adb -s {device} shell input keyevent {key}"
    status = run_command(command=command)
    if status['returncode'] == 0:
        return True
    else:
        return False
def scroll_height(device: str, x: int,y1: int, y2: int, duration: int=300)->bool:
    command = f"adb -s {device} shell input swipe {x} {y1} {x} {y2} {duration}"
    status = run_command(command=command)
    if status['returncode'] == 0:
        return True
    else:
        return False
def scroll_width(device: str, x1: int, x2: int, y: int, duration: int=300)->bool:
    command = f"adb -s {device} shell input swipe {x1} {y} {x2} {y} {duration}"
    status = run_command(command=command)
    if status['returncode'] == 0:
        return True
    else:
        return False
def scroll_up_or_down(device: str, x: int, y1: int, y2: int,type: Literal["up","down"]="up", duration: int=300)->bool:
    if type == "up":
        if scroll_height(device, x, y1, y2, duration):
            return True
        else:
            return False
    else:
        if scroll_height(device, x, y2, y1, duration):
            return True
        else:
            return False
def scroll_left_or_right(device: str, x1: int, x2: int, y: int,type: Literal["left","right"]="left", duration: int=300)->bool:
    if type == "left":
        if scroll_width(device, x1, x2, y, duration):
            return True
        else:
            return False
    else:
        if scroll_width(device, x2, x1, y, duration):
            return True
        else:
            return False
def scroll_top_or_bottom(device: str, x_screen: int, y_screen: int, type_scroll: Literal["up", "down"] = "up", duration: int=300)->bool:
    x= int(x_screen/2)
    y1 = int(y_screen*8/9)
    y2 = int(y_screen/10)
    if type_scroll == "up":
        if scroll_height(device, x, y1, y2, duration):
            return True
        else:
            return False
    else:
        if scroll_height(device, x, y2, y1, duration):
            return True
        else:
            return False

def scroll_top_or_bottom_short(device: str, x_screen: int, y_screen: int,type_scroll: Literal["up", "down"] = "up",  duration: int=300)->bool:
    x= int(x_screen/2)
    y1 = int(y_screen/2)
    y2 = int(y_screen/9)
    if type_scroll == "up":
        if scroll_height(device, x, y1, y2, duration):
            return True
        else:
            return False
    else:
        if scroll_height(device, x, y2, y1, duration):
            return True
        else:
            return False

def scroll_center_up_or_down(device: str, x_screen: int, y_screen: int, type_scroll: Literal["up", "down"] = "up",  duration: int=300)->bool:
    x= int(x_screen/2)
    y1 = int(y_screen/4)
    y2 = int(y_screen*3/4)
    if type_scroll == "up":
        if scroll_height(device, x, y2, y1, duration):
            return True
        else:
            return False
    else:
        if scroll_height(device, x, y1, y2, duration):
            return True
        else:
            return False
def scroll_center_up_or_down_short(device: str, x_screen: int, y_screen: int, type_scroll: Literal["up", "down"] = "up",  duration: int=300)->bool:
    x= int(x_screen/2)
    y1 = int(y_screen/4)
    y2 = int(y_screen*3/5)
    if type_scroll == "up":
        if scroll_height(device, x, y2, y1, duration):
            return True
        else:
            return False
    else:
        if scroll_height(device, x, y1, y2, duration):
            return True
        else:
            return False
def long_press(device: str, x: int, y: int, duration: int=1000)-> bool:
    command = f"adb -s {device} shell input swipe {x} {y} {x} {y} {duration}"
    status = run_command(command=command)
    if status['returncode'] == 0:
        return True
    else:
        return False

def open_app(device, package)-> bool:
    command = f"adb -s {device} shell monkey -p {package} 1"
    status = run_command(command=command)
    if status['returncode'] == 0:
        return True
    else:
        return False


def close_app(device: str, package: str)-> bool:
    command = f"adb -s {device} shell am force-stop {package}"
    status = run_command(command=command)
    if status['returncode'] == 0:
        return True
    else:
        return False

def clear_cache(device: str)-> bool:
    command = f"adb -s {device} shell pm clear {device}"
    status =run_command(command=command)
    if status['returncode'] == 0:
        return True
    else:
        return False