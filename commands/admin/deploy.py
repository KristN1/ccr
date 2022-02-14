import os
from discord.ext import commands

from conf._config import Config
from lib.embed import BaseEmbed

class Deploy(commands.Cog):

    def __init__(self, client, config: Config):
        self.client = client
        self.config = config

    @commands.command()
    async def deploy(self, ctx):
        os.system("screen -dmS ccr-deploy")
        os.system("sudo chmod +x /home/kristn/python_stuff/ccr/ccr_venv/bot/commands/admin/deploy.sh")
        os.system("screen -S ccr-deploy -X stuff '/home/kristn/python_stuff/ccr/ccr_venv/bot/commands/admin/deploy.sh\n'")


def setup(client, config):
    client.add_cog(Deploy(client, config))