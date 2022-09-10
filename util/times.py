# -*- coding: utf-8 -*-

import time
import datetime

DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
DATE_FORMAT = "%Y-%m-%d"
TIME_FORMAT = "%H:%M:%S"


class Times:

    # 当前毫秒数
    @staticmethod
    def current_millisecond():
        return int(time.time() * 1000)

    # 当前秒数
    @staticmethod
    def current_timestamp():
        return int(time.time())

    # 当前日期  格式%Y-%m-%d %H:%M:%S
    @staticmethod
    def current_datetime():
        return datetime.datetime.strftime(datetime.datetime.now(), DATETIME_FORMAT)

    # 当前日期  格式%Y-%m-%d
    @staticmethod
    def current_date():
        return datetime.datetime.strftime(datetime.datetime.now(), DATE_FORMAT)

    # 当前时间  格式%Y-%m-%d
    @staticmethod
    def current_time():
        return datetime.datetime.strftime(datetime.datetime.now(), TIME_FORMAT)

    @staticmethod
    def datetime_to_timestamp(datetime_string):
        d = datetime.datetime.strptime(datetime_string, DATETIME_FORMAT)
        t = d.timetuple()
        return int(time.mktime(t))

    @staticmethod
    def timestamp_to_datetime(timestamp):
        return datetime.datetime.fromtimestamp(timestamp)

    @staticmethod
    def datetime_to_string(date_time, date_format=DATETIME_FORMAT):
        return datetime.datetime.strftime(date_time, date_format)


if __name__ == '__main__':
    print(Times.timestamp_to_datetime(1655913600))
