from discord.ext import commands

from lib.embed import BaseEmbed

class MemberLeave(commands.Cog):
    def __init__(self, client, config):
        self.client = client
        self.config = config

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        membercount_channel = self.client.get_channel(self.config.membercount_channel)
        join_leave_channel = self.client.get_channel(self.config.join_leave_channel)

        embed = BaseEmbed(self.client, 
        title = "Member left!",
        description = f"{member.name} was done with losing and left the server.\n\nMembercount: {member.guild.member_count}",
        color = 0xa80004).generate()
        embed.set_thumbnail(url=member.avatar_url)

        await join_leave_channel.send(embed=embed)
        await membercount_channel.edit(name=f"Members: {member.guild.member_count}")
        
def setup(client, config):
    client.add_cog(MemberLeave(client, config))