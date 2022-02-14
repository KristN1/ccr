import discord
from discord.ext import commands

from lib import load_cogs
from conf._config import Config

config = Config()
intents = discord.Intents().all()
client = commands.Bot(command_prefix=config.prefix, intents=intents)
load_cogs.run(client, config)

client.run(config.tokens.discord)