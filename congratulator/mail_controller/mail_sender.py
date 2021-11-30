from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from common.logger import logger as log


def send(target, name):
    sender = 'ivansp1971@mail.ru'

    message = f'Dear, {name}!\n\nHappy birthday!\n\nBest regards,\nCongratulator'
    msg = MIMEText(message)
    msg['Subject'] = 'Congratulation'
    msg['From'] = sender
    msg['To'] = ', '.join(target)
    try:
        server = SMTP_SSL('smtp.mail.ru', 465)
        server.login(sender, 'vP8Aw8LaAkGzEx64s55d')
        server.sendmail(sender, target, msg.as_string())
        return True
    except Exception:
        log.info(f'Can\'t send email to {target}')
        return False
    finally:
        server.quit()


if __name__ == '__main__':
    send(['lena_bess@list.ru'], 'Elena')
