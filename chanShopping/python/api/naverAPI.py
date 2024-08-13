import requests
import json
import os


class NaverAPI():
    def __init__(self):
        self.API_ID = os.getenv("API_ID")
        self.API_SECRET = os.getenv("API_SECRET")
        self.url = "https://openapi.naver.com/v1/search/shop.json?"
        self.queryString = "query="
        self.headers = {
            "X-Naver-Client-Id": self.API_ID,
            "X-Naver-Client-Secret": self.API_SECRET
        }

    def searchItem(self,product):
        request = requests.get(url=self.url + self.queryString + product, headers=self.headers)
        try:
            items = json.loads(request.text)["items"]
            return items
        except KeyError:
            return None
