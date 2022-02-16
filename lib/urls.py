import json

urlsfile = "./conf/urls.json"

def add(url: str):
    with open(urlsfile, "r") as f:
        urls = json.load(f)
    urls.append(url)
    with open(urlsfile, "w") as f:
        json.dump(urls, f, indent=4)

def remove(url: str):
    with open(urlsfile, "r") as f:
        urls = json.load(f)
    try:
        urls.remove(url)
    except ValueError:
        pass
    with open(urlsfile, "w") as f:
        json.dump(urls, f, indent=4)