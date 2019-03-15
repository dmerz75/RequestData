from datetime import datetime
from datetime import timedelta


def get_date_range(date, **kwargs):

    if 'format' in kwargs:
        date_format = kwargs['format']
    else:
        date_format = '%Y-%m-%d'

    if 'days' in kwargs:
        days = kwargs['days']
    else:
        days = 7

    # print(date)
    # print(date_format)
    # print(days)
    # sys.exit()

    end_dt = datetime.strptime(date, date_format)
    start_dt = end_dt + timedelta(days=days)
    # print(start_dt, end_dt)

    end_date = str(end_dt)[0:10]
    start_date = str(start_dt)[0:10]
    # print(start_date, end_date)

    return start_date, end_date