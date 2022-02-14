import json

conf_dir = "./conf"

tokens_conf = conf_dir + "/tokens.json"
topics_conf = conf_dir + "/topics.json"
general_conf = conf_dir + "/general.json"
tickets_conf = conf_dir + "/tickets.json"
urls_conf = conf_dir + "/urls.json"


class Config():
    def __init__(self):
        self.tokens = self.Tokens(self.open_file(tokens_conf))

        self.topics = self.open_file(topics_conf)

        self.prefix = self.open_file(general_conf)["prefix"]
        self.admins = self.open_file(general_conf)["admins"]
        self.membercount_channel = self.open_file(general_conf)["membercount_channel"]
        self.link_logs_channel = self.open_file(general_conf)["link_logs_channel"]

        self.tickets = self.Tickets(self.open_file(tickets_conf))
        
        self.whitelisted_urls = self.open_file(urls_conf)

    def open_file(self, filepath: str):
        with open(filepath, "r",) as f:
            return json.load(f)

    class Tokens():
        def __init__(self, tokens):
            self.discord = tokens["discord"]

    class Tickets():
        def __init__(self, config):
            self.reaction_message = self.ReactionMessage(config["reaction_message"])
            self.roles = self.Roles(config["roles"])
            self.new_tickets = self.CreateTickets(config["new_tickets"])

        class ReactionMessage():
            def __init__(self, config):
                self.channel_ids = config["channel_ids"]
                self.message_ids = config["message_ids"]
                self.emoji = config["emoji"]

        class Roles():
            def __init__(self, config):
                self.ping = config["ping"]
                self.staff = config["staff"]
                self.new = config["new"]

        class CreateTickets():
            def __init__(self, config):
                self.category = config["category"]