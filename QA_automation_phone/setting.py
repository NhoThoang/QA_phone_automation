from QA_automation_phone.config import config
class setting(config):
    def __init__(self,device: str = None, connect = None, x_screen: int = None, y_screen: int = None) -> None:
        super().__init__(device=device, connect=connect, x_screen=x_screen, y_screen=y_screen)
        self.device = device
    def open_setting(self, setting: str):
        command = f'adb -s {self.device} shell am start -a android.settings.{setting}'
        self.run_command(command=command)
    def open_setting_display(self):
        self.open_setting('DISPLAY_SETTINGS')
    def open_setting_sound(self):
        self.open_setting('SOUND_SETTINGS')
    def open_setting_storage(self):
        self.open_setting('INTERNAL_STORAGE_SETTINGS')
    def open_setting_battery(self):
        self.open_setting('BATTERY_SAVER_SETTINGS')
    def open_setting_location(self):
        self.open_setting('LOCATION_SOURCE_SETTINGS')
    def open_setting_security(self):
        self.open_setting('SECURITY_SETTINGS')
    def open_setting_language(self):
        self.open_setting('LOCALE_SETTINGS')
    def open_setting_keyboard(self):
        self.open_setting('INPUT_METHOD_SETTINGS')
    def open_setting_input(self):
        self.open_setting('INPUT_METHOD_SETTINGS')
    def open_setting_date_time(self):
        self.open_setting('DATE_SETTINGS')
    def open_setting_accessibility(self):
        self.open_setting('ACCESSIBILITY_SETTINGS')

    def open_setting_application(self):
        self.open_setting('APPLICATION_SETTINGS')
    def open_setting_development(self):
        self.open_setting('APPLICATION_DEVELOPMENT_SETTINGS')
    def open_setting_device_info(self):
        self.open_setting('DEVICE_INFO_SETTINGS')
    def open_setting_about_phone(self):
        self.open_setting('ABOUT_PHONE')
    def open_setting_reset(self):
        self.open_setting('BACKUP_RESET_SETTINGS')

    def open_setting_reset_network(self):
        self.open_setting('NETWORK_OPERATOR_SETTINGS')
    def open_setting_reset_app(self):
        self.open_setting('APPLICATION_DETAILS_SETTINGS')
    def open_setting_wifi(self):
        self.open_setting('WIFI_SETTINGS')
    def open_setting_bluetooth(self):
        self.open_setting('BLUETOOTH_SETTINGS')
    def open_account_manager(self):
        self.open_setting('ACCOUNT_SETTINGS')

    def open_setting_print(self):
        self.open_setting('PRINT_SETTINGS')
    def open_add_account(self):
        self.open_setting('ADD_ACCOUNT_SETTINGS')
    def open_setting_app(self):
        self.open_setting('SETTINGS')

    # permission 