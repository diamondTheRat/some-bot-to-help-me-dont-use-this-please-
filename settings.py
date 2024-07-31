from json import load
from functools import reduce


def load_settings():
    with open("settings.json") as f:
        settings = load(f)

    color = settings["color"]
    color = reduce(lambda x, y: x << 8 | y, color)
    settings['color'] = color

    return settings