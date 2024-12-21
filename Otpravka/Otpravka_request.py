import requests
import json

from http.server import BaseHTTPRequestHandler, HTTPServer


server_ip = 'http://localhost:5005/api/user'
#server_ip = 'http://192.168.1.150:5005/api/user'
#server_ip = 'https://www.example.com/'
headers = {'Content-Type': 'application/json'}

m = {
    "msg_type": "intro",
    "login_from": "@Aleksandra",
    "login_to": "192.168.14.134",
    "msg": "Proverka"
}

m1 = {
    "msg_type": "msg",
    "login_from": "@Aleksandra",
    "login_to": "@Anton",
    "msg": "Privet, Anton :)"
}

m4 = {
    "msg_type": "logins",
    "login_from": "@Mikhail",
    "login_to": "@ivan",
    "msg": "Proverka"
}

response = requests.post(server_ip, data=json.dumps(m), headers=headers)

