import discord
import datetime


class BaseEmbed():
    def __init__(self, client: discord.Client, title, description, color=None, timestamp=None, footer_text=None, footer_icon=None):
        self.title = title
        self.description = description
        self.color = color

        if color == None:
            color = 0x08ccfd
        self.color = color

        if timestamp == None:
            timestamp = datetime.datetime.now()
        self.timestamp = datetime.datetime.now()

        if footer_text == None:
            footer_text = client.user.name
        self.footer_text = footer_text

        if footer_icon == None:
            footer_icon = client.user.avatar_url
        self.footer_icon = footer_icon

    def generate(self):
        embed=discord.Embed(title=self.title, description=self.description, color=self.color)
        embed.timestamp = self.timestamp
        embed.set_footer(text=self.footer_text, icon_url=self.footer_icon)

        return embed