import discord
from discord.ext import commands
from lib import embed

class Message(commands.Cog):
    def __init__(self, client, config):
        self.client = client
        self.config = config

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author != self.client:

            if message.content == f"<@!{self.client.user.id}>" or message.content == f"<@{self.client.user.id}>":
                await message.channel.send(f"Hey there, my prefix is **{self.config.prefix}**")

            if message.channel.id == 659823869720264714:
                reactions = ["<a:check:722817478119653458>", "<a:nocheck:722817545362735145>"]
                for emoji in reactions:
                    await message.add_reaction(emoji)

            if "http" in message.content.lower():
                domains = message.content.lower().split("http")
                
                for domain in domains:
                    domain = domain.split(" ")[0]
                    if "://" in domain:
                        domain = domain.split("://")[1].split("/")[0].split(".")[-2:]
                        domain = ".".join(domain)
                        staffrole = discord.utils.get(message.guild.roles, id=self.config.tickets.roles.staff)

                        whitelisted = False
            
                        if domain in self.config.whitelisted_urls:
                            whitelisted = True


                        if whitelisted != True:
                            if message.author.bot == False:
                                if staffrole not in message.author.roles:
                                    await message.delete()

                                link_logs_channel = self.client.get_channel(self.config.link_logs_channel)
                                msg = await link_logs_channel.send(embed=embed.BaseEmbed(self.client, "Link detected", f"Author - {message.author.mention}\nID - {message.author.id}\nChannel - {message.channel.mention}\n\nURL - https://{domain}", 0xff8040, None, message.author.name, message.author.avatar_url).generate())
                                break
        
def setup(client, config):
    client.add_cog(Message(client, config))