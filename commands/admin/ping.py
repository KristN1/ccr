import discord
import datetime
from discord.ext import commands

from conf._config import Config
from lib.embed import BaseEmbed

class Ping(commands.Cog):

    def __init__(self, client, config: Config):
        self.client = client
        self.config = config

    @commands.command()
    async def ping(self, ctx):
        bot_name = self.client.user.name
        bot_pfp = self.client.user.avatar_url

        embed=discord.Embed(color=0x08ccfd)
        embed.add_field(name="Pong", value=f"Latency is `{round(self.client.latency * 1000)}` ms", inline=False)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=bot_name, icon_url=bot_pfp)

        await ctx.send(embed=BaseEmbed(
                                client = self.client,
                                title = "Pong",
                                description = f"Latency is `{round(self.client.latency * 1000)}` ms",
                                color = None,
                                timestamp = None,
                                footer_text = None,
                                footer_icon = None).generate())
        

def setup(client, config):
    client.add_cog(Ping(client, config))