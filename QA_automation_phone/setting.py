from QA_automation_phone.config import run_command
def open_setting(device: str, setting: str):
    command = f'adb -s {device} shell am start -a android.settings.{setting}'
    run_command(command=command)
def open_setting_display(device: str):
    open_setting(device, 'DISPLAY_SETTINGS')
def open_setting_sound(device: str):
    open_setting(device, 'SOUND_SETTINGS')
def open_setting_storage(device: str):
    open_setting(device, 'INTERNAL_STORAGE_SETTINGS')
def open_setting_battery(device: str):
    open_setting(device, 'BATTERY_SAVER_SETTINGS')
def open_setting_location(device: str):
    open_setting(device, 'LOCATION_SOURCE_SETTINGS')
def open_setting_security(device: str):
    open_setting(device, 'SECURITY_SETTINGS')
def open_setting_language(device: str):
    open_setting(device, 'LOCALE_SETTINGS')
def open_setting_keyboard(device: str):
    open_setting(device, 'INPUT_METHOD_SETTINGS')
def open_setting_input(device: str):
    open_setting(device, 'INPUT_METHOD_SETTINGS')
def open_setting_date_time(device: str):
    open_setting(device, 'DATE_SETTINGS')
def open_setting_accessibility(device: str):
    open_setting(device, 'ACCESSIBILITY_SETTINGS')

def open_setting_application(device: str):
    open_setting(device, 'APPLICATION_SETTINGS')
def open_setting_development(device: str):
    open_setting(device, 'APPLICATION_DEVELOPMENT_SETTINGS')
def open_setting_device_info(device: str):
    open_setting(device, 'DEVICE_INFO_SETTINGS')
def open_setting_about_phone(device: str):
    open_setting(device, 'ABOUT_PHONE')
def open_setting_reset(device: str):
    open_setting(device, 'BACKUP_RESET_SETTINGS')

def open_setting_reset_network(device: str):
    open_setting(device, 'NETWORK_OPERATOR_SETTINGS')
def open_setting_reset_app(device: str):
    open_setting(device, 'APPLICATION_DETAILS_SETTINGS')
def open_setting_wifi(device: str):
    open_setting(device, 'WIFI_SETTINGS')
def open_setting_bluetooth(device: str):
    open_setting(device, 'BLUETOOTH_SETTINGS')
def open_account_manager(device: str):
    open_setting(device, 'ACCOUNT_SETTINGS')

def open_setting_print(device: str):
    open_setting(device, 'PRINT_SETTINGS')
def open_add_account(device: str):
    open_setting(device, 'ADD_ACCOUNT_SETTINGS')
def open_setting_app(device: str):
    open_setting(device, 'SETTINGS')

# permission 