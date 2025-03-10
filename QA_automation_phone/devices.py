from QA_automation_phone.config import run_command_text
def get_screen_size(device: str)->list:
    command = f"adb -s {device} shell wm size"
    size = run_command_text(command=command)
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
def get_devices()->list:
    # try:
    devices_list = run_command_text('adb devices')

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
   
def get_model(devices):
    models = []
    for device in devices:
        command = f'adb -s {device} shell getprop ro.product.model'
        result = run_command_text(command=command)
        if result['returncode'] == 0:
            models.append(result['stdout'])
    return models
