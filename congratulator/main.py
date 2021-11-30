import schedule
import time
from common.log_rotation import log_rotation
from mail_controller.make_congratulation import make_congratulation


schedule.every().day.at("11:11").do(make_congratulation)

while True:
    schedule.run_pending()
    log_rotation()
    time.sleep(60)
