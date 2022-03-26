from datetime import datetime, timedelta

import pytz

from models.connection import Connections


class ConnectionsCleaner:

    @staticmethod
    def create_departure_connection(connections):
        """This method creates a list of connections from a list of dictionnaries.
            The method get from the dictionnary the information needed.
            The information stored in connection list concern the connection departure data.
            Information not needed are not stored in Connection objects.
        Arguments:
            connection {List} -- Contains the dictionnaries.
        Returns:
            [List] -- List of departures between two station.
        """
        connections_list = [
            Connections(**{
                'id': connection.get('id', None),
                'delay': connection.get('departure', None).get('delay', None),
                'canceled': connection.get('departure', None).get('canceled', None),
                'time': connection.get('departure', None).get('time', None),
                'station': connection.get('departure', None).get('station', None)

            }
            ) for connection in connections['connection']]

        return connections_list

    @staticmethod
    def remove_timeslot_overrun(connections_list, timeslot):
        """This methodd removes connection object between two station, if the connection object time is over
        a certain timeslot.

        Args:
            connections_list (List): List of connection object between two station
            timeslot (Integer): number of hours

        Returns:
            result (List): List of departures before a timeslot.
        """
        result = []
        for connection in connections_list:

            connection_time_converted = datetime.fromtimestamp(
                int(connection.time), tz=pytz.timezone('Europe/Brussels'))
            connection_time_converted_plus_one_hour = datetime.now(
                pytz.timezone('Europe/Brussels')) + timedelta(hours=timeslot)

            if connection_time_converted <= connection_time_converted_plus_one_hour:
                result.append(connection)

        return result
