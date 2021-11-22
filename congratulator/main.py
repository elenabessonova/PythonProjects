import schedule
import time
from congratulator.mail_controller.make_congratulation import make_congratulation


schedule.every().day.at("11:11").do(make_congratulation)

while True:
    schedule.run_pending()
    time.sleep(60)
