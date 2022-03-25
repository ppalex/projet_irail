from .api import ConnectionsApi
from .payload import ConnectionsPayload
from .cleaner import ConnectionsCleaner


class ConnectionsAPIManager:
    def __init__(self):
        """Constructor of the class ConnectionsAPIManager.
        """
        self.data = None

    def download_connections_data(self, station_from, station_to):
        """This method download connections from a particular station to
            another station.
             The data are recovered in self.data.

        Arguments:
            station_from {string} -- station from.
            station_to {string} -- station to.
        """

        headers = {}

        api = ConnectionsApi()
        payload = ConnectionsPayload(
            station_from=station_from, station_to=station_to)

        connections = api.send_request(
            headers, payload.get_payload_formatted())
        connections_cleaned = ConnectionsCleaner.create_departure_connection(
            connections)

        self.data = connections_cleaned

    @staticmethod
    def get_total_connections(connections_list):
        return len(connections_list)

    @staticmethod
    def get_total_connections_canceled(connections_list):
        return len([connection for connection in connections_list
                    if connection.canceled == "1"])

    @staticmethod
    def next_hour_train_running(connections_list):

        connections_list = ConnectionsCleaner.remove_timeslot_overrun(
            connections_list, timeslot=1)
        total_running_train = ConnectionsAPIManager.get_total_connections(
            connections_list)
        total_canceled_train = ConnectionsAPIManager.get_total_connections_canceled(
            connections_list)

        return ((total_running_train - total_canceled_train) /
                total_running_train) * 100

    @staticmethod
    def next_hour_train_delay(connections_list):
        pass
