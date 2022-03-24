class Connections:
    """Constructor of the class Connections.
    """

    def __init__(self, **connections_attributes):
        """Constructor of the class Connections.
        """
        for attr_name, attr_value in connections_attributes.items():
            setattr(self, attr_name, attr_value)
