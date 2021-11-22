import datetime as dt
from congratulator.db_controller import db_configure
from congratulator.mail_controller import mail_sender
from congratulator.common.loger_config import loger


def make_congratulation():
    user_list = db_configure.load_users()
    today = dt.date.today()
    for user in user_list:
        date = dt.datetime.strptime(user[1], '%d.%m')
        loger.debug(f'date {date.day}.{date.month}, today {today}')

        if dt.datetime.strptime(user[1], '%d.%m').day == today.day and \
                dt.datetime.strptime(user[1], '%d.%m').month == today.month:
            mail_sender.send([user[2]], user[0])
            loger.info(f'mail send to {user[0]}')


if __name__ == '__main__':
    make_congratulation()
