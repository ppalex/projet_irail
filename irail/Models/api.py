import logging

import configuration.config as config
import requests

config.load()


class ConnectionsApi:
    def __init__(self):
        """Constructor of the class Connections Api."""

        self.base_url = config.value['API']['url']

        self.endpoint = {
            "connections":  "connections/"
        }
        self.data = []

    def send_request(self, headers, payload):
        """This method send a request on the connection api end point.
        Args:
            headers (String)
            payload (String)
        Raises:
            SystemExit: If exception is raised.
        Returns:
            [JSON]: Response from the request. Contains the data.
        """
        try:
            response = requests.get(
                self.base_url + self.endpoint['connections'],
                headers=headers,
                params=payload)

        except requests.exceptions.Timeout:
            logging.error("Timeout error", exc_info=True)
        except requests.exceptions.TooManyRedirects:
            logging.error("Bad url", exc_info=True)
        except requests.exceptions.RequestException as e:
            logging.error("Bad request", exc_info=True)
            raise SystemExit(e)

        if response.status_code == 200:
            self.data = response.json()
            return response.json()
        else:
            return None
