import discord
from discord import message
from conf._config import Config

import commands.admin.ping as ping
import commands.admin.ticket_setup as ticket_setup
import commands.admin.wl as wl
import commands.fun.topic as topic

import events.advanced.raw_reaction_add as reaction_add
import events.basic.member_join as member_join
import events.basic.member_leave as member_leave
import events.basic.ready as ready
import events.basic.message as message


def run(client: discord.Client, config: Config):
    ping.setup(client, config)
    ticket_setup.setup(client, config)
    wl.setup(client, config)
    topic.setup(client, config)

    reaction_add.setup(client, config)
    member_join.setup(client, config)
    member_leave.setup(client, config)
    ready.setup(client, config)
    message.setup(client, config)
