from discord.ext import commands

from conf._config import Config
import lib.urls

class Ping(commands.Cog):

    def __init__(self, client, config: Config):
        self.client = client
        self.config = config

    @commands.command()
    async def wl(self, ctx, action: str, argument: str = None):
        if action.lower() == "add":
            if argument is not None:
                lib.urls.add(argument.lower())
                await ctx.send("Added to whitelist")
            else:
                await ctx.send("Please specify a url")

        elif action.lower() == "remove":
            if argument is not None:
                lib.urls.remove(argument.lower())
                await ctx.send("Removed from whitelist")
            else:
                await ctx.send("Please specify a url")
        
        elif action == "list":
            urls = lib.urls._list()

            urls_str = "```"
            for url in urls:
                urls_str += url + "\n"
            urls_str += "```"
            
            await ctx.send(urls_str)
        else:
            await ctx.send("Invalid action, use `add` or `remove`")

def setup(client, config):
    client.add_cog(Ping(client, config))