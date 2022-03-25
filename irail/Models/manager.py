from models.cleaner import ConnectionsCleaner
from models.payload import ConnectionsPayload


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

        api = ConnectionsAPIManager()
        payload = ConnectionsPayload(
            station_from=station_from, station_to=station_to)

        connections = api.send_request(
            headers, payload.get_payload_formatted())
        connections_cleaned = ConnectionsCleaner.create(connections)

        self.data = connections_cleaned
