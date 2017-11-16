# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 2017

@author: fernando.teixeira
"""



def iguana_uncertainty_get(token=None, fonte=None, datainicio=None,
                           datafim=None, categoria=None, nmec=None,
                           output = ["error","message","data"]):
    url_base = 'http://iguana.incertezalab.com/incerteza?token='
    
    assert(token is not None), "É preciso inserir um token valido! \n Solicite em www.iguana.incertezalab.com/documentation/index.php"
    if fonte is None and datainicio is None and datafim is None and categoria is None:
        
        dados = url_base + token
        dados_fin = requests.get(dados).json()
        
        
    params = []

    if fonte is not None: 
        params.append("&fonte=" + fonte)
        
    if datainicio is not None: 
        params.append("&datainicio=" + datainicio)
        
        
    if datafim is not None: 
        params.append("&datafim=" + datafim)

    if limite is not None: 
        params.append("&limite=" + limite)

    if categoria is not None: 
        params.append("&categoria=" + categoria)

    if nmec is not None: 
        params.append("&nmec=" + nmec)

    
    #corrigir esse .join
    dados = url_base + token + .join(params)
    dados_fin = requests.get(dados).json()    
    if len(output == 3):
        
    else:
        if("error" in output):
        elif("message" in output):
        elif("data" in output):
        

    return dados_fin['data']
