from datetime import datetime, timedelta
import pytz


def get_percent_next_hour_train_running(manager):
    """_summary_

    Args:
        manager (_type_): _description_

    Returns:
        _type_: _description_
    """    
    return manager.next_hour_train_running(manager.data)


def get_mean_next_hour_train_delay(manager):
    return manager.next_hour_train_delay(manager.data)


def get_number_past_2_hour_train_canceled(manager):
    return manager.get_total_connections_canceled(manager.data)


def create_results(from_station,
                   to_station,
                   next_hour_running,
                   next_hour_train_delay,
                   past_2_hours_canceled):

    dict = {
        "from_station": from_station,
        "to_station": to_station,
        "next_hour_running": next_hour_running,
        "next_hour_train_delay": next_hour_train_delay,
        "past_2_hours_canceled": past_2_hours_canceled
    }

    return dict


def get_past_2_hour_time():
    time_now = datetime.now(tz=pytz.timezone('Europe/Brussels'))
    time_now_min_2 = time_now - timedelta(hours=2)
    time_now_min_2_formatted = time_now_min_2.strftime("%H%M")

    return time_now_min_2_formatted
