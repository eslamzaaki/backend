import requests 


def test1(url):
    res=requests.get(url)
    return res.json()
