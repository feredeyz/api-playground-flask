import requests
from scripts.functions import get_celcium
class WeatherApi:
    def __init__(self):
        self.__api_key = '№'
    def get_weather(self, city):
        res = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={self.__api_key}")
        if res.json()["cod"] != '404':
            return int(get_celcium(res.json()["main"]["temp"]))
        return 'City not found.' 
    
class CatApi:
    def __init__(self):
        self.__api_key = '№'
        self.__url = f'https://api.thecatapi.com/v1/images/search?limit=1&has_breed=0&api_key={self.__api_key}'
    def get_cat(self):
        res = requests.get(self.__url)
        return res.json()[0]["url"]
    
class DogApi:
    def __init__(self):
        self.__api_key = '№'
        self.__url = f'https://api.thedogapi.com/v1/images/search?limit=1&has_breed=0&api_key={self.__api_key}'
    def get_dog(self):
        res = requests.get(self.__url)
        return res.json()[0]["url"]