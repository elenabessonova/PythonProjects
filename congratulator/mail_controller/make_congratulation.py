import datetime as dt
from db_controller import db_configure
from db_controller import db_create
from mail_controller import mail_sender
from common.logger import logger as log
import os


def make_congratulation(db_user_list):
    today = dt.date.today()
    for user in db_user_list:
        date = dt.datetime.strptime(user[1], '%d.%m')
        log.debug(f'date {date.day}.{date.month}, today {today}')

        if dt.datetime.strptime(user[1], '%d.%m').day == today.day and \
                dt.datetime.strptime(user[1], '%d.%m').month == today.month:
            mail_sender.send([user[2]], user[0])
            log.info(f'mail send to {user[0]}')


if __name__ == '__main__':
    make_congratulation(db_create.db_create('congrats.db'))
