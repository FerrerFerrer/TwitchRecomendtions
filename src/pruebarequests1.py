# -*- coding: utf-8 -*-

import requests
import twitch
from twitch import TwitchHelix, TwitchClient


client = TwitchHelix(client_id= 'vnsbdjciw4fcif1k57w1c07a65wk03', oauth_token= 'oauth:17qyf4koyvfdqjs4me7zr451lccmtn')

HEADS = {
    "Accept" : "application/vnd.twitchtv.v5+json",
    "Client-ID" : "vnsbdjciw4fcif1k57w1c07a65wk03"
    #"Authorization" : "OAuth 17qyf4koyvfdqjs4me7zr451lccmtn"
}

nombre = "pokimane"
URL = "https://api.twitch.tv/kraken/users?login={}".format(nombre)
r = requests.get(url = URL, headers = HEADS)

temp = r.json()
try:
    id = temp["users"][0]["_id"]
    print(id)
    t = client.get_user_follows(from_id = id)

    for i in t:
        print(i["to_name"])
except:
    print("Some error occured")
#print(client.get_user_follows(from_id = "118237854"))
#print(client.get)
