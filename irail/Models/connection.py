class Connections:
    """Constructor of the class Connections.
    """

    def __init__(self, **connections_attributes):
        """Constructor of the class Connections.
        """
        for attr_name, attr_value in connections_attributes.items():
            setattr(self, attr_name, attr_value)

    def __str__(self):
        """This method return an object Connections in String format
        """
        string = ""
        attr = vars(self)
        for k, v in attr.items():
            string += f"{k} : {v} \n"
        return string
