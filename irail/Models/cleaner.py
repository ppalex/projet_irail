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
            [List] -- List of Product.
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
