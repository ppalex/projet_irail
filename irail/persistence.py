import json
import os
from pathlib import Path

RESULT_DIRECTORY = Path(__file__).parent.parent / "data"


def save_data(result_dict):

    from_station = result_dict["from_station"]
    to_station = result_dict["to_station"]

    with open(
        os.path.join(
            RESULT_DIRECTORY,
            f"to_{from_station}_from_{to_station}.json"), "w") as outfile:
        json.dump(result_dict, outfile, indent=4)
