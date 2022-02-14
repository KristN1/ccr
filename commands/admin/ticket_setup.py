import asyncio
from discord.ext import commands

from conf._config import Config
from lib.embed import BaseEmbed
from conf import _ticket_setup as ticket_setup

class TicketSetup(commands.Cog):

    def __init__(self, client, config: Config):
        self.client = client
        self.config = config

    @commands.command()
    async def send_ticket(self, ctx, category: str):
        if category.lower()  == "verify":
            if ctx.author.id in self.config.admins:
                await ctx.message.delete()
                message = await ctx.send(embed=BaseEmbed(
                                        client = self.client,
                                        title = "👋 __Welcome!__",
                                        description = f"In order to get verified and receive the correct roles we require you to open a ticket.\nReact with {self.config.tickets.reaction_message.emoji} to open a ticket please!",
                                        color = 0x3584e4,
                                        timestamp = None,
                                        footer_text = None,
                                        footer_icon = None).generate())
                
                
                await message.add_reaction(self.config.tickets.reaction_message.emoji)

                #ticket_setup.setup_reaction_message(message.channel.id, message.id)

        elif category.lower() == "staffhelp":
            if ctx.author.id in self.config.admins:
                await ctx.message.delete()
                message = await ctx.send(embed=BaseEmbed(
                                        client = self.client,
                                        title = "Open a ticket",
                                        description = self.config.tickets.entry_messages.help,
                                        color = 0x57e389,
                                        timestamp = None,
                                        footer_text = None,
                                        footer_icon = None).generate())
                
                
                await message.add_reaction(self.config.tickets.reaction_message.emoji)

                #ticket_setup.setup_reaction_message(message.channel.id, message.id)
        else:
            await ctx.send("Invalid category, select from `verify` or `staffhelp`")
            await asyncio.sleep(3)

            await ctx.channel.purge(limit=2)

def setup(client, config):
    client.add_cog(TicketSetup(client, config))