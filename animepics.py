import requests


def get_waifu_pic():
    response = requests.get("https://api.waifu.pics/sfw/waifu")
    response = response.json()
    response = response["url"]
    return response
