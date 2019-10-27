import requests
import twitch
from twitch import TwitchHelix

#client = twitch.(client_id= 'vnsbdjciw4fcif1k57w1c07a65wk03', oauth_token= 'oauth:17qyf4koyvfdqjs4me7zr451lccmtn')


r = requests.get('https://api.twitch.tv/helix/users?', auth =('vnsbdjciw4fcif1k57w1c07a65wk03', 'oauth:17qyf4koyvfdqjs4me7zr451lccmtn'))
print(r.text)