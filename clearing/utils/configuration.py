import os
import json


def load_config(filename):
    if os.path.exists(filename):
        try:
            return json.load(open(filename, 'rb'))
        except ValueError:
            return {}
    else:
        return {}


def update_config(filename, cnf):
    config = load_config(filename)
    config.update(cnf)
    json.dump(config, open(filename, "wb"))
