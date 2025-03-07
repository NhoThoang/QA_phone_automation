from QA_automation_phone.config import run_command

class settings:
    def __init__(self, device=None) -> None:
        self.device = device
    def open_setting_date(self):
        command=f'adb -s {self.device} shell am start -a android.settings.DATE_SETTINGS'
        run_command(command=command)
