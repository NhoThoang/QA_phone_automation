from QA_automation_phone.config import config
import re
class script(config):
    def __init__(self,device: str = None, connect = None, x_screen: int = None, y_screen: int = None) -> None:
        super().__init__(device, connect, x_screen, y_screen)
        self.device = device
        self.connect = connect
        self.x_screen = x_screen
        self.y_screen = y_screen
    def extract_apk(self, package_name: str, output: str) -> bool:
        path_command = f"adb -s {self.device} shell pm path {package_name}"
        result = self.run_command_text(path_command)
        if result['returncode'] == 0:
            path = re.search(r'package:(.+)', result['stdout']).group(1)
            command = f"adb -s {self.device} pull {path} {output}"
            self.run_command(command=command)
            return True
        else:
            return False
    def check_status_screen(self)->bool:
        command = f"adb -s {self.device} shell dumpsys display"
        result = self.run_command_text(command=command)
        if result['returncode'] == 0:
            return "mCurrentFocus" in result['stdout']
        else:
            return False
    def get_logs(self, output: str)->bool:
        command = f"adb -s {self.device} logcat -b all -d > {output}"
        result = self.run_command(command=command)
        if result['returncode'] == 0:
            return True
        else:
            return False
    def clear_all_logs(self)->bool:
        command = f"adb -s {self.device} logcat -c"
        result = self.run_command(command=command)
        if result['returncode'] == 0:
            return True
        else:
            return False
    def screen_shot(self, output: str)->bool:
        command = f"adb -s {self.device} exec-out screencap -p > {output}"
        result = self.run_command(command=command)
        if result['returncode'] == 0:
            return True
        else:
            return False

    def set_screen_timeout(self, timeout: int=15)->bool:
        command = f"adb -s {self.device} shell settings put system screen_off_timeout {timeout*1000}"
        result = self.run_command(command=command)
        if result['returncode'] == 0:
            return True
        else:
            return False
    def on_format_24h(self)->bool:
        command = f"adb -s {self.device} shell settings put system time_12_24 24"
        result = self.run_command(command=command)
        if result['returncode'] == 0:
            return True
        else:
            return False
    def off_format_24h(self)->bool:
        command = f"adb -s {self.device} shell settings put system time_12_24 12"
        result = self.run_command(command=command)
        if result['returncode'] == 0:
            return True
        else:
            return False
    def on_auto_update_time(self)->bool:
        command = f"adb -s {self.device} shell settings put system auto_time 1"
        result = self.run_command(command=command)
        if result['returncode'] == 0:
            return True
        else:
            return False
    def off_auto_update_time(self)->bool:
        command = f"adb -s {self.device} shell settings put system auto_time 0"
        result = self.run_command(command=command)
        if result['returncode'] == 0:
            return True
        else:
            return False
        
