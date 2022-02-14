import random
from discord.ext import commands

from conf._config import Config
from lib.embed import BaseEmbed

class Topic(commands.Cog):

    def __init__(self, client, config: Config):
        self.client = client
        self.config = config

    @commands.command()
    async def topic(self, ctx):
        await ctx.send(embed=BaseEmbed(
                                client = self.client,
                                title = "Topic",
                                description = random.choice(self.config.topics),
                                color = 0x465356,
                                timestamp = None,
                                footer_text = None,
                                footer_icon = None).generate())

def setup(client, config):
    client.add_cog(Topic(client, config))