from QA_automation_phone.config import run_command, run_command_text
import re
def extract_apk(device: str, package_name: str, output: str) -> bool:
    path_command = f"adb -s {device} shell pm path {package_name}"
    result = run_command_text(path_command)
    if result['returncode'] == 0:
        path = re.search(r'package:(.+)', result['stdout']).group(1)
        command = f"adb -s {device} pull {path} {output}"
        run_command(command=command)
        return True
    else:
        return False
def check_status_screen(device: str)->bool:
    command = f"adb -s {device} shell dumpsys display"
    result = run_command_text(command=command)
    if result['returncode'] == 0:
        return "mCurrentFocus" in result['stdout']
    else:
        return False
def get_logs(device: str, output: str)->bool:
    command = f"adb -s {device} logcat -b all -d > {output}"
    result = run_command(command=command)
    if result['returncode'] == 0:
        return True
    else:
        return False
def clear_all_logs(device: str)->bool:
    command = f"adb -s {device} logcat -c"
    result = run_command(command=command)
    if result['returncode'] == 0:
        return True
    else:
        return False
def screen_shot(device: str, output: str)->bool:
    command = f"adb -s {device} exec-out screencap -p > {output}"
    result = run_command(command=command)
    if result['returncode'] == 0:
        return True
    else:
        return False

def set_screen_timeout(device: str, timeout: int=15)->bool:
    command = f"adb -s {device} shell settings put system screen_off_timeout {timeout*1000}"
    result = run_command(command=command)
    if result['returncode'] == 0:
        return True
    else:
        return False
def on_format_24h(device: str)->bool:
    command = f"adb -s {device} shell settings put system time_12_24 24"
    result = run_command(command=command)
    if result['returncode'] == 0:
        return True
    else:
        return False
def off_format_24h(device: str)->bool:
    command = f"adb -s {device} shell settings put system time_12_24 12"
    result = run_command(command=command)
    if result['returncode'] == 0:
        return True
    else:
        return False
def on_auto_update_time(device: str)->bool:
    command = f"adb -s {device} shell settings put system auto_time 1"
    result = run_command(command=command)
    if result['returncode'] == 0:
        return True
    else:
        return False
def off_auto_update_time(device: str)->bool:
    command = f"adb -s {device} shell settings put system auto_time 0"
    result = run_command(command=command)
    if result['returncode'] == 0:
        return True
    else:
        return False
    
