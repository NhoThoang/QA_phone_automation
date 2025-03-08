import subprocess
import xml.etree.ElementTree as ET
import uiautomator2 as u2
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
        'stdout': stdout.strip(),
        'stderr': stderr.strip(),
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

def adb_click(device: str,x:int,y:int):
    command = f"adb -s {device} shell input tap {x} {y}"
    run_command(command=command)
def adb_send(device: str,content: str):
    command = f"adb -s {device} shell input text {content}"
    run_command(command=command)
def adb_click_send(device: str,x:int,y:int,content:str):
    adb_click(device, x, y)
    adb_send(device, content)
def adb_keyevent(device: str,key: int):
    command = f"adb -s {device} shell input keyevent {key}"
    run_command(command=command)
def scroll_height(device: str, x: int,y1: int, y2: int, distance: int=300):
    command = f"adb -s {device} shell input swipe {x} {y1} {x} {y2} {distance}"
    run_command(command=command)
def scroll_width(device: str, x1: int, x2: int, y: int, distance: int=300):
    command = f"adb -s {device} shell input swipe {x1} {y} {x2} {y} {distance}"
    run_command(command=command)
def scroll_up_down(device: str,type: Literal["up","down"], x: int, y1: int, y2: int, distance: int=300):
    if type == "up":
        scroll_height(device, x, y1, y2, distance)
    else:
        scroll_height(device, x, y2, y1, distance)
def scroll_left_right(device: str,type: Literal["left","right"], x1: int, x2: int, y: int, distance: int=300):
    if type == "left":
        scroll_width(device, x1, x2, y, distance)
    else:
        scroll_width(device, x2, x1, y, distance)
def scroll_top(device: str, x_screen: int, y_screen: int,  distance: int=300):
    x= x_screen/2
    y1 = y_screen*8/9
    y2 = y_screen/10
    scroll_height(device, x, y1, y2, distance)
def scroll_bottom(device: str, x_screen: int, y_screen: int,  distance: int=300):
    x= x_screen/2
    y1 = y_screen/10
    y2 = y_screen*8/9
    scroll_height(device, x, y1, y2, distance)
def scroll_top_short(device: str, x_screen: int, y_screen: int,  distance: int=300):
    x= x_screen/2
    y1 = y_screen/2
    y2 = y_screen/9
    scroll_height(device, x, y1, y2, distance)
def scroll_bottom_short(device: str, x_screen: int, y_screen: int,  distance: int=300):
    x= x_screen/2
    y1 = y_screen/9
    y2 = y_screen/2
    scroll_height(device, x, y1, y2, distance)




def long_press(device: str, x: int, y: int, duration: int=1000):
    command = f"adb -s {device} shell input swipe {x} {y} {x} {y} {duration}"
    run_command(command=command)
def open_app(device: str, package_name: str):
    command = f"adb -s {device} shell am start -n {package_name}"
    run_command(command=command)

def open_app2(device, package):
    command = f"adb -s {device} shell monkey -p {package} 1"
    run_command(command=command)

def close_app(device: str, package_name: str):
    command = f"adb -s {device} shell am force-stop {package_name}"
    run_command(command=command)
def clear_cache(device: str):
    command = f"adb -s {device} shell pm clear {device}"
    run_command(command=command)