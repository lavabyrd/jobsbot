import json


def pretty_json(json_data):
    """
    allows JSON to be dumped into the terminal in a clean way
    """
    return json.dumps(
        json_data, sort_keys=True, indent=4, separators=(',', ': ')
    )
