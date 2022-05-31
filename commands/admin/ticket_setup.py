import datetime
import asyncio
from discord.ext import commands

from conf._config import Config
from lib.embed import BaseEmbed

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
                                        timestamp = datetime.datetime.utcnow(),
                                        footer_text = self.client.user.name,
                                        footer_icon = None).generate())
                
                
                await message.add_reaction(self.config.tickets.reaction_message.emoji)

                #ticket_setup.setup_reaction_message(message.channel.id, message.id)

        elif category.lower() == "staffhelp":
            if ctx.author.id in self.config.admins:
                await ctx.message.delete()
                message = await ctx.send(embed=BaseEmbed(
                                        client = self.client,
                                        title = "Open a ticket",
                                        description = "Hello,\nHow can we help you? Our staff team will be ready for you when you open a ticket!\n⚠️ Please read our FAQ and <#623213850644316210> before opening a ticket, you might get an answer there.\n\nValid reasons to open a ticket:\n<:reddot:892477402020712449> Claim a role\n<:reddot:892477402020712449> Get added to <#911340112858742794>\n<:reddot:892477402020712449> Partnerships & sponsorships\n<:reddot:892477402020712449> Report a bug or a member\n<:reddot:892477402020712449> Unanswered questions",
                                        color = 0x57e389,
                                        timestamp = datetime.datetime.utcnow(),
                                        footer_text = self.client.user.name,
                                        footer_icon = self.client.user.avatar_url).generate())
                
                
                await message.add_reaction(self.config.tickets.reaction_message.emoji)

                #ticket_setup.setup_reaction_message(message.channel.id, message.id)
        else:
            await ctx.send("Invalid category, select from `verify` or `staffhelp`")
            await asyncio.sleep(3)

            await ctx.channel.purge(limit=2)

def setup(client, config):
    client.add_cog(TicketSetup(client, config))