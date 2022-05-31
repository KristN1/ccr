import discord
from discord.ext import commands
from discord.raw_models import RawReactionActionEvent

from lib.embed import BaseEmbed
from lib.custom_payload import CustomPayload

lock_emoji = "🔒"

class RawReactionAdd(commands.Cog):
    def __init__(self, client, config):
        self.client = client
        self.config = config

    async def create_ticket(self, payload: discord.RawReactionActionEvent, current_msg: discord.Message, guild: discord.Guild):
        try:
            await current_msg.remove_reaction(payload.emoji, payload.member)
        except:
            pass

        await self.create_ticket_channel(guild, payload, f"🎫-{payload.member.name.lower()}")

    async def create_ticket_channel(self, guild: discord.Guild, payload: RawReactionActionEvent, channel_name: str):
        staff_role = discord.utils.get(guild.roles, id=self.config.tickets.roles.staff)
        ping_role = discord.utils.get(guild.roles, id=self.config.tickets.roles.ping)
        muted_role = discord.utils.get(guild.roles, id=self.config.tickets.roles.muted)
        bots_role = discord.utils.get(guild.roles, id=self.config.tickets.roles.bots)

        create_perms = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            guild.me: discord.PermissionOverwrite(read_messages=True),
            payload.member: discord.PermissionOverwrite(read_messages=True),
            staff_role: discord.PermissionOverwrite(read_messages=True),
            muted_role: discord.PermissionOverwrite(send_messages=True),
            bots_role: discord.PermissionOverwrite(read_messages=True)
            }

        category = discord.utils.get(self.client.get_guild(guild.id).categories, id=self.config.tickets.new_tickets.category)
        ticket_channel = await guild.create_text_channel(channel_name, overwrites=create_perms, category=category)
        ping = await ticket_channel.send(f"{payload.member.mention} {ping_role.mention}")
        await ping.delete()

        new_role = guild.get_role(self.config.tickets.roles.new)
        if new_role in payload.member.roles:
            message = f"""
            <a:shiny_sparkles:811198225494573075> <a:wave_blob:811198487898619924> Welcome {payload.member.mention}

            Before you get access to the server we need to ask you some questions.
            Please answer below in order to get the correct roles.
            A staffmember will be here shortly!

            <a:animated_dirt:811198385276715018> - What is your Minecraft name?
            <a:cube_shiny:811198292481802250> - Do you play CUbeCraft bedrock, java, both or neither?
            <a:levelup:811198009014485023> - What is your CubeCraft level?
            <:takemymoney:811197908422492190> - Which rank do you own? (Java exclusive)
            <:leaderboard:811197955885236253> - Are you on any leaderboards? How many?
            """
        else:
            message = f"""<a:wave_blob:811198487898619924> Hi {payload.member.mention}! How can we help you?"""

        ticket_embed=BaseEmbed(                                
                        client = self.client,
                        title = "New ticket",
                        description = message,
                        color = 0x3584e4,
                        timestamp = None,
                        footer_text = f"To close this ticket, react with {lock_emoji}",
                        footer_icon = None).generate()

        ticket_msg = await ticket_channel.send(embed=ticket_embed)
        await ticket_msg.add_reaction(lock_emoji)


    async def delete_ticket(self, current_msg: discord.Message, current_channel: discord.TextChannel, payload: RawReactionActionEvent):
        await current_msg.remove_reaction(lock_emoji, payload.member)
        await current_channel.send("Deleting...")
        await current_channel.delete()


    async def checks(self, payload: discord.RawReactionActionEvent):
        guild = self.client.get_guild(payload.guild_id)
        reaction_channel = guild.get_channel(payload.channel_id)
        reaction_message = await reaction_channel.fetch_message(payload.message_id)

        if payload.user_id != self.client.user.id:

            if str(payload.emoji) == self.config.tickets.reaction_message.emoji:
                if reaction_channel.id in self.config.tickets.reaction_message.channel_ids:
                    if reaction_message.id in self.config.tickets.reaction_message.message_ids:
                        if await self.has_ticket(guild, f"🎫-{payload.member.name.lower()}") == False:
                            await self.create_ticket(payload, reaction_message, guild)
                        else:
                            await reaction_message.remove_reaction(payload.emoji, payload.member)

            elif str(payload.emoji) == lock_emoji:
                for reaction in reaction_message.reactions:
                    if str(reaction.emoji) == lock_emoji:
                        reaction_users = await reaction.users().flatten()
                        if self.client.user in reaction_users:
                            await reaction_message.remove_reaction(lock_emoji, payload.member)
                            staffrole = discord.utils.get(guild.roles, id=self.config.tickets.roles.staff)
                            if staffrole in payload.member.roles:
                                await self.delete_ticket(reaction_message, reaction_channel, payload)
    
    async def has_ticket(self, guild: discord.Guild, channel_name: str):
        for channel in guild.channels:
            if channel.name == channel_name:
                return True

        return False

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        await self.checks(payload)

    @commands.command(aliases=["reaction"])
    async def verify(self, ctx):
        payload = CustomPayload(ctx)
        if await self.has_ticket(ctx.guild, f"🎫-{ctx.author.name.lower()}") == False:
            await self.create_ticket(payload, ctx.message, ctx.guild)
        else:
            await ctx.send("You already have a ticket open.")



def setup(client, config):
    client.add_cog(RawReactionAdd(client, config))