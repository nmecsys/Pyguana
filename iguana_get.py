import requests
import json


token = 'k2rt3f5'

def iguana_get(token=None, fonte=None, datainicio=None, datafim=None, categoria=None):
    url_base = 'http://iguana.incertezalab.com/jornais?token='
    assert(token is not None)
    if fonte is None and datainicio is None and datafim is None and categoria is None:
        
        dados = url_base + token
        dados = requests.get(dados).json()
        dados = json.loads(dados)
    return dados


iguana_get(token = token)
