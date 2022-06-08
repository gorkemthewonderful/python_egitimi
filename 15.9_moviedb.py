#anahtar kelimeye göre arama
#vizyondakiler
#en popülerler.

import re
from subprocess import list2cmdline
import requests
import json

class Movie:
    def populars(self):
        popularsUrl = ("https://api.themoviedb.org/3/movie/popular?api_key=7afa7257d00d0d096cfaf043bda37b31&language=en-US&page=1")
        responseP = requests.get(popularsUrl)
        return responseP.json()
    def nowplaying(self):
        nowplayingUrl = ("https://api.themoviedb.org/3/movie/now_playing?api_key=7afa7257d00d0d096cfaf043bda37b31&language=en-US&page=1")
        response = requests.get(nowplayingUrl)
        return response.json()
    def keywordmovie(self):
        movie_id = input("Film ismi giriniz: ")
        keywordUrl = (f"https://api.themoviedb.org/3/movie/{movie_id}/keywords?api_key=7afa7257d00d0d096cfaf043bda37b31")
        response = requests.get(keywordUrl)
        return response.json()
       
movieApi = Movie()

while True:
    secim = input("1- Popular Movies\n2- Now Playing\n3- Keyword\n4- Exit\nSeçim: ")
    if secim == "4":
        break
    else:
        if secim == "1":
            movies = movieApi.populars()
            for movie in movies["results"]:
                print (movie["title"])
        elif secim == "2":
            movies = movieApi.nowplaying()
            for movie in movies["results"]:
                print(movie["title"])
        elif secim == "3":
            movies = movieApi.keywordmovie()
            for movie in movies["results"]:
                print(movie["title"])      #3 ü çalıştıramadım.





















