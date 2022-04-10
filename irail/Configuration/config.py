"""Module for configuring the application.
The configuration is read from a YAML file and saved in a module-global
variable.
"""

import yaml
import os
from pathlib import Path
import logging
import sys

"""Load the config file"""

CONFIG_DIRECTORY = Path(__file__).parent.parent / "configuration"
CONFIG_FILE = "config.yaml"

value = {}  # Global var, not constant


def load():
    """Loads a configuration file into a module-global variable.
    The module-global variable is a dict named `value`. If several files are
    loaded sequentially, the dict is updated (not overwritten).
    Args:
        config_path (str): path of the YAML configuration file.
    """
    config_env_file = open(os.path.join(CONFIG_DIRECTORY, CONFIG_FILE), 'r')
    config_content = yaml.load(config_env_file, Loader=yaml.FullLoader)

    env = config_content.get("ENV")

    try:
        with open(os.path.join(CONFIG_DIRECTORY, f"config-{env}.yaml"), 'r') as config_file:
            value.update(yaml.load(config_file, Loader=yaml.FullLoader))

    except FileNotFoundError:
        logging.error("File not found: verify config file", exc_info=True)
        sys.exit(1)
