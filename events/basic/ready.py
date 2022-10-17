from discord.ext import commands

class Ready(commands.Cog):
    def __init__(self, client, config):
        self.client = client
        self.config = config

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"ID - {self.client.user.id}")
        print(f"Username - {self.client.user.name}")
        print("Is ready")
        print("pterodactyl_running")
        
def setup(client, config):
    client.add_cog(Ready(client, config))