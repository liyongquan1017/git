import requests

url = "http://192.168.51.236:5050/api/test"

payload = "url=%2Fapi%2Fv2%2Fgamecenter%2FgetMiniGameList&params=%7B%0A%20%20%20%20%22uid%22%3A%20%2210838559%22%2C%0A%20%20%20%20%22__appid_%22%3A%20%2210002%22%2C%0A%20%20%20%20%22__channelId_%22%3A%20-1%2C%0A%20%20%20%20%22__appVersion_%22%3A%20%2280614%22%2C%0A%20%20%20%20%22position%22%3A%200%0A%7D"
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache",
    'postman-token': "2a911238-1ad1-e58f-2d73-f61465c3d3f7"
}

response = requests.request("POST", url, data=payload, headers=headers).json()
code = response.get('code')
print(code)
print(type(code))
print(response)