import schedule
import time
from common.log_rotation import log_rotation
from mail_controller.make_congratulation import make_congratulation
from db_controller.db_create import db_create


schedule.every().day.at("14:36").do(make_congratulation, db_create('congrats.db'))

while True:
    schedule.run_pending()
    log_rotation()
    time.sleep(60)
