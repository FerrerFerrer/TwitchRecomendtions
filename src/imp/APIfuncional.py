from abs.absAPI import AbstactClassApi
import twitch
from twitch import TwitchClient, TwitchHelix
import requests

class apiTwitch(AbstactClassApi):
    def __init__(self, *args):
        super().__init__(*args)
        self.helix = TwitchHelix(client_id= 'vnsbdjciw4fcif1k57w1c07a65wk03', oauth_token= 'oauth:17qyf4koyvfdqjs4me7zr451lccmtn')
        self.client = TwitchClient(client_id= 'vnsbdjciw4fcif1k57w1c07a65wk03', oauth_token= 'oauth:17qyf4koyvfdqjs4me7zr451lccmtn')

    def get_userid(self, username):
        nombre = username
        URL = "https://api.twitch.tv/kraken/users?login={}".format(nombre)
        r = requests.get(url = URL, headers = self.HEADS)
        temp = r.json()
        id_usuario = temp["users"][0]["_id"]
        #############################################################
        return id_usuario

    def get_followers(self, id_cliente):
        namefollows = []
        t = self.helix.get_user_follows(from_id = id)
        namefollows = []
        for i in t:
            namefollows.append(i["to_id"])
        #print(namefollows)
        return namefollows

    def get_name(self, id_streamer):
       pass

    def get_followe(self, id_streamer):
        self.id_streamer = id_streamer
        seguidoresStreamer = self.client.channels.get_by_id(id_streamer)
        cantidad = seguidoresStreamer["followers"]
        return cantidad

if __name__ == '__main__':
    workingapi = apiTwitch()
    prueba1 = workingapi.get_userid("albertto1198")
    print(prueba1)
