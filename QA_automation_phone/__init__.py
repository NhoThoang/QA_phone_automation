from QA_automation_phone.config import config
from QA_automation_phone.coreapp import coreapp, u2
from QA_automation_phone.identify_letter import identify_letter
from QA_automation_phone.identify_image import identify_image
from QA_automation_phone.keyevent import keyevent
from QA_automation_phone.setting import setting
from QA_automation_phone.script import script

process = config()
def get_devices()->list:
    # try:
    devices_list = process.run_command_text('adb devices')
    if devices_list['returncode'] == 0:
        devices_list = devices_list['stdout'].split('\n')[1:]
    decvices = []
    for device in devices_list:
        if "device" in device:
            try:
                decvices.append(device.split('\t')[0].strip(" "))
            except Exception as e:
                print("Error: ",e)
    return decvices
def get_model(devices: list)->list:
    models = []
    for device in devices:
        command = f'adb -s {device} shell getprop ro.product.model'
        result = process.run_command_text(command=command)
        if result['returncode'] == 0:
            models.append(result['stdout'])
    return models
class connect(coreapp, identify_letter, identify_image, keyevent, setting, script, config):
# class connect(coreapp, identify_image, identify_letter, keyevent, setting, script, config):
    def __init__(self, device: str = None) -> None:
        if device == None:
            self.device = get_devices()
            if self.device:
                self.device = self.device[0]
        else:
            self.device = device
        if self.device:
            x_screen, y_screen = self.get_screen_size()
            x_screen = int(x_screen); y_screen = int(y_screen)
            self.connect = u2.connect(self.device)
            super().__init__(device=self.device, connect=self.connect, x_screen=x_screen, y_screen=y_screen)
        else:
            raise Exception("Device not found")

    def get_screen_size(self)->list:
        command = f"adb -s {self.device} shell wm size"
        size = self.run_command_text(command=command)
        if size['returncode'] == 0:
            size = size['stdout']
            type_size = "Over"
            if type_size in size:
                size = size.split("\n")
                if len(size) > 1:
                    for text in size:
                        if type_size in text:
                            return text.split(":")[1].strip().split("x")
                else:
                    return size.split(":")[1].strip().split("x")
            else:
                return size.split(":")[1].strip().split("x")

   

  