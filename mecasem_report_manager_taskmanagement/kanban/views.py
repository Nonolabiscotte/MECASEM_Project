from django.shortcuts import render, HttpResponse
from django.template import loader
import requests
import time

#rest_framework

from rest_framework import status
from rest_framework.response import Response

import requests
import json

# Create your views here.

def main(request):
    return HttpResponse("You're at home")

def dnd(request):
    template = loader.get_template('kanban/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def get_affair(request):
    url="http://127.0.0.1:8080/affair"
    #r = requests.get(url, headers={'Authorization': 'Bearer %s' % 'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ1c2VyIiwiZXhwIjoxNjA2NzA0MzY5fQ.QEgF3smIh629KNR9lyZvix81YMcku1g8mDd28uo9r1hRPFNDf0HNWSNTzvKuaOhp22vURv0RIH6hOTMUb4kMpg'})
    r = requests.get(url, headers={'Authorization': 'Bearer %s' % generate_token()})
    droplets = r.json()
    droplet_list = []
    for key in droplets:
        droplet_list.append(droplets[key])
    return HttpResponse(droplet_list)

#generate a valid token to use the API
def generate_token():
    url = "http://127.0.0.1:8080/auth/login"
    data = {'password': 'password', 'username': 'user'}
    r = requests.post(url, json=data)
    token = json.loads(r.text)["token"]
    return token

def test(request):
    return HttpResponse("hello!")

# une affaire = un kanban
