import json
import os
from pathlib import Path

RESULT_DIRECTORY = Path(__file__).parent.parent / "data"


def save_data(data_dict):
    """This function saves a dictionary into a JSON file.

    Args:
        data_dict (Dict): Contains the results
    """    

    from_station = data_dict['from_station']
    to_station = data_dict['to_station']

    with open(
        os.path.join(
            RESULT_DIRECTORY,
            f"from_{from_station}_to_{to_station}.json"), "w") as outfile:
        json.dump(data_dict, outfile, indent=4)
