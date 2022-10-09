from datetime import datetime


def convert_time_stamp(timestamp):
    timestamp = int(timestamp)
    dt_object = datetime.fromtimestamp(timestamp)
    return dt_object
