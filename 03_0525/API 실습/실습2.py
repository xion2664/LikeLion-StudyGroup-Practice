import requests

url = 'https://opendart.fss.or.kr/api/fnlttSinglAcntAll.json'
params = {'crtfc_key':'1ece02082edfad8bb704827c723b2c7b1e5e9e23',
          'corp_code':'00126380', 'bsns_year':'2022', 'reprt_code':'11014', 'fs_div':'CFS'}

res = requests.get(url,params)

print(res.status_code)
print(res.headers['content-type'])
print(res.encoding)
print(res.text)
print(res.json())

print(len(res.json()['list']))