import discord
from discord.ext import commands

from lib import cogs
from conf._config import Config

config = Config()
intents = discord.Intents().all()
client = commands.Bot(command_prefix=config.prefix, intents=intents)
cogs.load(client, config)

client.run(config.tokens.discord)