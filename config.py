import json
import os

with open("conf/tokens.json", "w") as f:
    json.dump({"discord": os.environ["DISCORD_TOKEN"]}, f, indent=4)