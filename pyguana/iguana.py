# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 2017

@author: fernando.teixeira
"""


import pandas as pd
import requests


class Iguana(object):
    
    def __init__(self, token):
        """Return a token string whose name is *token*."""
        self.token = token
    
    
    
    def get(self, fonte=None, datainicio=None, 
               datafim=None, categoria=None, limite=None):
    
        '''
        Teste, criando uma docstring.
        
        '''
        
        url_base = 'http://iguana.incertezalab.com/jornais?token='
        
        assert(token is not None), "É preciso inserir um token válido! \n Solicite em www.iguana.incertezalab.com/documentation/index.php"
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
    
        
        
        
        #corrigir esse .join
        dados = url_base + token + "".join([str(x) for x in params])
        dados_fin = requests.get(dados).json()
            
        
        
        return dados_fin['data']


    
    
    def uncertainty_get(self, token, fonte=None, datainicio=None,
                           datafim=None, categoria=None, nmec=None):
    
        url_base = 'http://iguana.incertezalab.com/incerteza?token='
        
        assert(token is not None), "É preciso inserir um token valido! \n Solicite em www.iguana.incertezalab.com/documentation/index.php"
        if fonte is None and datainicio is None and datafim is None and categoria is None:
            
            dados = url_base + token
            dados_fin = requests.get(dados).json()
            
        '''    
        if len(output) == 3:
            print("teste")    
            
        else:
            if "error" in output:
                print("error")
            if "message" in output:
                print("message")
            if "data" in output:
                print("data")
        '''
            
            
    
        return dados_fin['data']
    
    
    
    

    def reader(self, token, start, end, cenario = [1,2,3]):
        
        
    
        assert(token is not None), "É preciso inserir um token válido! \n Solicite em www.iguana.incertezalab.com/documentation/index.php"
        assert(start or end is None), "É necessario passar a janela de data das notícias!" 
        
        ##- valor online
        valor_online = pd.DataFrame(get(token=token,datainicio = start,datafim = end,fonte = "Valor_Economico"))['noticia']
        valor_online = leitor(valor_online, start_date=start,end_date=end)
        
        ##- valor impresso    
        valor_impresso = pd.DataFrame(get(token=token,datainicio = "2012",datafim = "2015",fonte = "Valor_impresso"))['noticia']
        valor_impresso = leitor(valor_impresso,start_date = start,end_date=end)
        ##- folha online
        folha_online = pd.DataFrame(get(token=token,datainicio = start,datafim = end,fonte = "Folha_online"))['noticia']
        folha_online = leitor(folha_online,start_date = start,end_date=end)
        ##- folha impresso
        folha_impresso = pd.DataFrame(get(token=token,datainicio = start,datafim = end,fonte = "Folha_impresso"))['noticia']
        folha_impresso = leitor(folha_impresso,start_date = start,end_date=end)
        ##- @estadao
        estadao  = pd.DataFrame(get(token=token,datainicio = start,datafim = end,fonte = "@estadao"))['noticia']
        estadao = leitor(estadao,start_date = start,end_date=end)
        ##- @correio
        correio  = pd.DataFrame(get(token=token,datainicio = start,datafim = end,fonte = "@correio"))['noticia']
        correio = leitor(correio,start_date = start,end_date=end)
        ##- @oglobo
        oglobo   = pd.DataFrame(get(token=token,datainicio = start,datafim = end,fonte = "@oglobo"))['noticia']
        oglobo = leitor(oglobo,start_date = start,end_date=end)
        ##- @zerohora
        zerohora = pd.DataFrame(get(token=token,datainicio = start,datafim = end,fonte = "zehora"))['noticia']
        zerohora = leitor(zerohora,start_date = start,end_date=end)
        
        return valor_online


token = 'k2rt3f5'
