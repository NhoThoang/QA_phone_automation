import time
import QA_automation_phone as qa
connect = qa.connect()
start = time.time()
connect.connect(text="Blood glucose").click()
print(time.time() - start)
# start = time.time()
# connect.click_element(value="Blood glucose")
# print(time.time() - start)