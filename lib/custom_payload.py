class CustomPayload():
    def __init__(self, ctx):
        self.channel_id = ctx.channel.id
        self.emoji = None
        self.event_type = None
        self.guild_id = ctx.guild.id
        self.member = ctx.author
        self.message_id = ctx.message.id
        self.user_id = ctx.author.id
        