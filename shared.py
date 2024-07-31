from settings import load_settings
import json


troll_messages = []
settings = load_settings()
temporary_channels = []

with open("reaction_roles.json") as f:
    reaction_roles = {int(key): value for key, value in json.load(f).items()}
