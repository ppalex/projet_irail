from models import ConnectionsAPIManager


def run():
    """
    """

    manager = ConnectionsAPIManager()
    manager.download_connections_data("Nivelles", "Charleroi")

    [print(c) for c in manager.data]


if __name__ == "__main__":
    """ Main function
    """
    run()
