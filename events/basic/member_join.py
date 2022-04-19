from discord.ext import commands

from lib.embed import BaseEmbed

class MemberJoin(commands.Cog):
    def __init__(self, client, config):
        self.client = client
        self.config = config

    @commands.Cog.listener()
    async def on_member_join(self, member):
        membercount_channel = self.client.get_channel(self.config.membercount_channel)
        join_leave_channel = self.client.get_channel(self.config.join_leave_channel)
        new_role = member.guild.get_role(self.config.tickets.roles.new)

        embed = BaseEmbed(self.client, 
        title = "Member joined!",
        description = f"Welcome {member.mention}\nWe hope you will have a good time enjoying our chats, playing minigames or competing in tournaments!\n\nMembercount: {member.guild.member_count}",
        color = 0x53d926).generate()
        embed.set_thumbnail(url=member.avatar_url)

        await member.add_roles(new_role)
        await join_leave_channel.send(embed=embed)
        await membercount_channel.edit(name=f"Members: {member.guild.member_count}")
        
def setup(client, config):
    client.add_cog(MemberJoin(client, config))