import json
ticket_conf = "./conf/tickets.json"

def setup_reaction_message(channel_id: int, message_id: int):
    with open(ticket_conf, "r") as f:
        config = json.load(f)

        config["reaction_message"]["channel_id"] = channel_id
        config["reaction_message"]["message_id"] = message_id

    with open(ticket_conf, "w") as f:
        json.dump(config, f, indent=4)