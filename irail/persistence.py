import json
import os
from pathlib import Path

RESULT_DIRECTORY = Path(__file__).parent.parent / "data"


def save_data(from_station, to_station, next_hour_running,
              next_hour_delay, past_2_hours_canceled):

    result_dict = {
        "from_station": from_station,
        "to_station": to_station,
        "next_hour_running": next_hour_running,
        "next_hour_delay": next_hour_delay,
        "past_2_hours_canceled": past_2_hours_canceled
    }

    with open(
        os.path.join(
            RESULT_DIRECTORY,
            f"from_{from_station}_to_{to_station}.json"), "w") as outfile:
        json.dump(result_dict, outfile, indent=4)
