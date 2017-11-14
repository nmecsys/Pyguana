import requests


token = 'k2rt3f5'

def iguana_get(token=None, fonte=None, datainicio=None, datafim=None, categoria=None):
    url_base = 'http://iguana.incertezalab.com/jornais?token='
    assert(token is not None), "You must provide a token to access the API."
    if fonte is None and datainicio is None and datafim is None and categoria is None:
        
        dados = url_base + token
        dados_fin = requests.get(dados).json()

    return dados_fin['data']


teste = iguana_get()
