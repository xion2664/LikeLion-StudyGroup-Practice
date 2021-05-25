import requests
import json

url = "https://kauth.kakao.com/oauth/token"

data = {
    "grant_type" : "authorization_code",
    "client_id" : "0830d56e8f269eeba378cdaf6946ffd3",
    "redirect_uri" : "https://localhost.com",
    "code"         : "cKLo4Ha0J2fFrI6B6rwDzj_4HEBv4i4I5bFtY4b6iDsyppnjUrubFZ8jyee0mZEGjDohWQo9cpcAAAF5os1RvQ"
    
}
response = requests.post(url, data=data)

tokens = response.json()

print(tokens)