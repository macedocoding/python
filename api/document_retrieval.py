#requests para testar requisições http e json para trabalhar com objeto JSON
from urllib import request
import requests as rq
import json

parameters = {
    'httpAccept': 'application/json',
    'APIKey': 'cf1f26157cab37737d22e365b8bc9c6b'
}

response = rq.get('https://api.elsevier.com/content/article/doi/10.1016/j.commatsci.2022.111487?', params=parameters)
print(response.status_code)


def jprint(obj):
    # Cria uma string formatada do objeto JSON
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


jprint(response.json())

