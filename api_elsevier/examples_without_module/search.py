import requests as rq
import json

parameters = {
    'query': 'aluminium',
    'apiKey': '7f59af901d2d86f78a1fd60c1bf9426a'
}

response = rq.get('https://api.elsevier.com/content/search/sciencedirect?', params=parameters)
print(response.status_code)


def jprint(obj):
    # Cria uma string formatada do objeto JSON
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


jprint(response.json())

