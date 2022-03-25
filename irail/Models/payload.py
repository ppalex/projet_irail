class ConnectionsPayload:

    """Constructor of the class Payload.
        Arguments:
        see: https://docs.irail.be/#connections

        """

    def __init__(self, station_from, station_to, timesel=None, typeOfTransport=None, time=None,
                 date=None, format="json", lang=None):

        self.station_from = station_from
        self.station_to = station_to
        self.timesel = timesel
        self.typeOfTransport = typeOfTransport
        self.time = time
        self.date = date
        self.format = format
        self.lang = lang

    def get_payload_formatted(self):
        """This method return an dictionnary representing a payload.
        Returns:
            [dict] -- Dict representing the payload for the GET Connctions API.
        """
        payload = {
            "from": self.station_from,
            "to": self.station_to,
            "timesel": self.timesel,
            "typeOfTransport": self.typeOfTransport,
            "time": self.time,
            "date": self.date,
            "format": self.format,
            "lang": self.lang
        }
        return payload
