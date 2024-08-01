
def get_current_hour():
    from datetime import datetime
    current_hour = datetime.now().hour
    return current_hour

def subtract_from_current_time(timestamp, hour_diff=0):
    from datetime import timedelta

    return timestamp - timedelta(hours=hour_diff)



def generate_today_date_string():
    from datetime import datetime
    today_date = datetime.now().strftime("%Y-%m-%d")
    return today_date


def create_datetime(set_year=None, set_month=None, set_day=None, set_hour=None):
    """
    Creates a datetime object with the given year, month, day, and hour.

    Args:
        set_year (int, optional): The year. Defaults to the current year.
        set_month (int, optional): The month (1-12). Defaults to the current month.
        set_day (int, optional): The day of the month. Defaults to the current day.
        set_hour (int, optional): The hour (0-23). Defaults to the current hour.

    Returns:
        datetime.datetime: A datetime object with the specified values.
    """
    from datetime import datetime

    current_datetime = datetime.now()

    if set_year is None:
        set_year = current_datetime.year
    if set_month is None:
        set_month = current_datetime.month
    if set_day is None:
        set_day = current_datetime.day
    if set_hour is None:
        set_hour = current_datetime.hour

    datetime_obj = datetime(
        year=set_year,
        month=set_month,
        day=set_day,
        hour=set_hour,
        minute=0,
        second=0,
        microsecond=0
    )
    return datetime_obj


def datetime_to_string(dt):
    """
    Convert a datetime object to a string with a normal time format.

    Parameters:
        dt (datetime.datetime): The datetime object to convert.

    Returns:
        str: The string representation of the datetime with normal time format.
    """
    # Convert datetime object to string with normal time format
    time_string = dt.strftime("%Y-%m-%d %H:%M:%S")
    return time_string


def string_to_datetime(time_string):
    """
    Convert a string with a normal time format to a datetime object.

    Parameters:
        time_string (str): The string representation of the datetime with normal time format.

    Returns:
        datetime.datetime: The datetime object converted from the string.
    """
    from datetime import datetime

    # Convert string to datetime object
    dt = datetime.strptime(time_string, "%Y-%m-%d %H:%M:%S")
    return dt

def utc_to_datetime(utc_timestamp):
    """
    Convert a UTC timestamp to a datetime.datetime object.

    Parameters:
    utc_timestamp (float): The UTC timestamp to convert.

    Returns:
    datetime.datetime: The corresponding datetime object in UTC.
    """
    from datetime import datetime, timezone
    dt = datetime.fromtimestamp(utc_timestamp, tz=timezone.utc)
    return dt
