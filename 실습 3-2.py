import requests
import json

url = "https://kauth.kakao.com/oauth/token"
data = {
    "grant_type" : "refresh_token",
    "client_id"  : "0830d56e8f269eeba378cdaf6946ffd3",
    "refresh_token" : "5pc6Lh5lokufro0SDxeeNib3wL0nabj5QhnE_Qo9c00AAAF5otLwQQ>"
}
response = requests.post(url, data=data)

print(response.json())