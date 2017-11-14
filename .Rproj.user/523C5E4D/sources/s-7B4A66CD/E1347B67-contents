# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 2017

@author: fernando.teixeira
"""



token = 'k2rt3f5'

def iguana_get(token=None, fonte=None, datainicio=None, datafim=None, categoria=None):
    url_base = 'http://iguana.incertezalab.com/jornais?token='
    assert(token is not None), "É preciso inserir um token valido! \n Solicite em www.iguana.incertezalab.com/documentation/index.php"
    if fonte is None and datainicio is None and datafim is None and categoria is None:
        
        dados = url_base + token
        dados_fin = requests.get(dados).json()

    return dados_fin['data']


# teste = iguana_get()
