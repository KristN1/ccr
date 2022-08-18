import sys
import json
import discord
from discord.ext import commands

from lib import cogs
from conf._config import Config

config = Config()
intents = discord.Intents(messages=True, members=True, guilds=True, reactions=True)
client = commands.Bot(command_prefix=config.prefix, intents=intents)
cogs.load(client, config)

try:
    with open("./conf/tokens.json", "r") as f:
        tokens = json.load(f)
        client.run(tokens["discord"])
except FileNotFoundError:
    client.run(sys.argv[1])