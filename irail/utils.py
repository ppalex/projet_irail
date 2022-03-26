from datetime import datetime, timedelta
import pytz


def get_percent_next_hour_train_running(manager):
    """This function return the percent of train running for the next hour.

    Args:
        manager (Object): Contains data after download from iRail API.

    Returns:
        Float: Contains a number witch represents percent.
    """
    return manager.next_hour_train_running(manager.data)


def get_mean_next_hour_train_delay(manager):
    """This function return the mean of train delayed for the next hour.

    Args:
        manager (Object): Contains data after download from iRail API.

    Returns:
        Float: Contains a number witch represents mean.
    """
    return manager.next_hour_train_delay(manager.data)


def get_number_past_2_hour_train_canceled(manager):
    """This function return train canceled during the past two hours.

    Args:
        manager (Object): Contains data after download from iRail API.

    Returns:
        Integer: Contains a number witch represents the number of train canceled.
    """
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
    """This function return the percent of train running for the next hour.

    Args:
        manager (Object): Contains data after download from iRail API.

    Returns:
        Float: Contains a number witch represents percent.
    """
    time_now = datetime.now(tz=pytz.timezone('Europe/Brussels'))
    time_now_min_2 = time_now - timedelta(hours=2)
    time_now_min_2_formatted = time_now_min_2.strftime("%H%M")

    return time_now_min_2_formatted
