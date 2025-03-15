
import QA_automation_phone as qa
devices = qa.get_devices()
cn = qa.connect(devices[0])
a= cn.orc_find_text(target_text="Samsung", lang="eng", index=1,click=True)
cn.orc_find_text(target_text="Settings", lang="eng", index=1,click=True)
cn.orc_scroll_find_text(target_text="Heart rate", click=True)
cn.orc_scroll_up_and_dow_find_text(target_text="Heart rate", click=True)
print(a)