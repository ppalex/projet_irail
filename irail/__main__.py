import configuration.config as config
from models import ConnectionsAPIManager
from persistence import save_data
from pathlib import Path
import os
from utils import (create_results, get_mean_next_hour_train_delay,
                   get_number_past_2_hour_train_canceled, get_past_2_hour_time,
                   get_percent_next_hour_train_running)


config.load()


def run(from_station, to_station):
    """
    This function calls components to retrieve data and the three main functionalities,
    it creates the result, and save the data.
    """

    connection_manager = ConnectionsAPIManager()

    connection_manager.download_connections_data(from_station, to_station)

    next_hour_running = get_percent_next_hour_train_running(connection_manager)

    next_hour_train_delay = get_mean_next_hour_train_delay(connection_manager)

    connection_manager.download_connections_data(
        from_station, to_station, time=get_past_2_hour_time())

    past_2_hours_canceled = get_number_past_2_hour_train_canceled(
        connection_manager)

    results = create_results(
        from_station,
        to_station,
        next_hour_running,
        next_hour_train_delay,
        past_2_hours_canceled

    )

    save_data(results)


if __name__ == "__main__":
    """ Main function
    """
    connections = config.value['CONNECTIONS']

    for line in connections.values():

        station_1, station_2 = line[0], line[1]

        run(station_1, station_2)
        run(station_2, station_1)
