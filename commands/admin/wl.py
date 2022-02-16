from discord.ext import commands

from conf._config import Config
import lib.urls, lib.urls

class Whitelist(commands.Cog):

    def __init__(self, client, config: Config):
        self.client = client
        self.config = config

    @commands.command()
    async def wl(self, ctx, action: str, argument: str = None):
        if ctx.author.id in self.config.admins:
            if action.lower() == "add":
                if argument is not None:
                    lib.urls.add(argument.lower())
                    self.reload_config()
                    await ctx.send("Added to whitelist")

                else:
                    await ctx.send("Please specify a url")

            elif action.lower() == "remove":
                if argument is not None:
                    lib.urls.remove(argument.lower())
                    self.reload_config()

                    await ctx.send("Removed from whitelist")
                else:
                    await ctx.send("Please specify a url")
            
            elif action == "list":
                urls = self.config.whitelisted_urls

                urls_str = "```"
                for url in urls:
                    urls_str += url + "\n"
                urls_str += "```"
                
                await ctx.send(urls_str)
            else:
                await ctx.send("Invalid action, use `add` or `remove`")
        else:
            raise commands.errors.MissingPermissions("You are not an admin")
    
    def reload_config(self):
        self.client.remove_cog("Whitelist")
        self.client.add_cog(Whitelist(self.client, Config()))

def setup(client, config):
    client.add_cog(Whitelist(client, config))