# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 2017

@author: fernando.teixeira
"""


import pandas as pd
import requests
import pyguana


'''
    A função get permite que se faça uma requisição à API Iguana, desde que possuindo um token
    válido, escolhendo todos os parâmetros que se deseja. Pode-se escolher a 'fonte' da notícia,
    ou seja, o jornal; é também possível delimitar uma data de início de uma de fim para o retorno
    das notícias e de que maneira ela foi categorizada pelo próprio jornal (em qual caderno a mesma
    se encontra). Exemplos de categoria seriam 'política', 'economia' ou 'esportes'.
    
'''


class Iguana(object):
    
    '''
        A função get permite que se faça uma requisição à API Iguana, desde que possuindo um token
        válido, escolhendo todos os parâmetros que se deseja. Pode-se escolher a 'fonte' da notícia,
        ou seja, o jornal; é também possível delimitar uma data de início de uma de fim para o retorno
        das notícias e de que maneira ela foi categorizada pelo próprio jornal (em qual caderno a mesma
        se encontra). Exemplos de categoria seriam 'política', 'economia' ou 'esportes'.
        
    '''
    
    def __init__(self, token):
        """Return a token string whose name is *token*."""
        self.token = token
    
    
    
    def get(self, fonte=None, datainicio=None, 
               datafim=None, categoria=None, limite=None):
    
        '''
        A função get permite que se faça uma requisição à API Iguana, desde que possuindo um token
        válido, escolhendo todos os parâmetros que se deseja. Pode-se escolher a 'fonte' da notícia,
        ou seja, o jornal; é também possível delimitar uma data de início de uma de fim para o retorno
        das notícias e de que maneira ela foi categorizada pelo próprio jornal (em qual caderno a mesma
        se encontra). Exemplos de categoria seriam 'política', 'economia' ou 'esportes'.
        
        '''
        
        url_base = 'http://iguana.incertezalab.com/jornais?token='
        
        assert(token is not None), "É preciso inserir um token válido! \n Solicite em www.iguana.incertezalab.com/documentation/index.php"
        if fonte is None and datainicio is None and datafim is None and categoria is None:
            
            dados = url_base + token

    
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
        dados_fin = pd.DataFrame(dados_fin['data'])    
        
        
        return dados_fin


    
    
    def uncertainty_get(self, fonte=None, datainicio=None,
                           datafim=None, categoria=None, nmec=None):
    
        url_base = 'http://iguana.incertezalab.com/incerteza?token='
        
        assert(token is not None), "É preciso inserir um token valido! \n Solicite em www.iguana.incertezalab.com/documentation/index.php"
        if fonte is None and datainicio is None and datafim is None and categoria is None:
            
            dados = url_base + token
            dados_fin = requests.get(dados).json()
            
        return dados_fin['data']
    
    
    
    

    def reader(self, start, end, cenario = [1,2,3]):
        
        # start='2010-01-01'
        # end='2011-03-01'
    
        assert(token is not None), "É preciso inserir um token válido! \n Solicite em www.iguana.incertezalab.com/documentation/index.php"
        assert(start or end is None), "É necessario passar a janela de data das notícias!" 
        
        ##- valor online
        valor_online = pd.DataFrame(pyguana.Iguana.get(self, datainicio = start,datafim = end,fonte = "Valor_Economico"))['noticia']
        valor_online = pyguana.leitor(valor_online, start_date=start,end_date=end)
        
        ##- valor impresso    
        valor_impresso = pd.DataFrame(pyguana.Iguana.get(token=token,datainicio = "2012",datafim = "2015",fonte = "Valor_impresso"))['noticia']
        valor_impresso = pyguana.leitor(valor_impresso,start_date = start,end_date=end)
        ##- folha online
        folha_online = pd.DataFrame(pyguana.Iguana.get(token=token,datainicio = start,datafim = end,fonte = "Folha_online"))['noticia']
        folha_online = pyguana.leitor(folha_online,start_date = start,end_date=end)
        ##- folha impresso
        folha_impresso = pd.DataFrame(pyguana.Iguana.get(token=token,datainicio = start,datafim = end,fonte = "Folha_impresso"))['noticia']
        folha_impresso = pyguana.leitor(folha_impresso,start_date = start,end_date=end)
        ##- @estadao
        estadao  = pd.DataFrame(pyguana.Iguana.get(token=token,datainicio = start,datafim = end,fonte = "@estadao"))['noticia']
        estadao = pyguana.leitor(estadao,start_date = start,end_date=end)
        ##- @correio
        correio  = pd.DataFrame(pyguana.Iguana.get(token=token,datainicio = start,datafim = end,fonte = "@correio"))['noticia']
        correio = pyguana.leitor(correio,start_date = start,end_date=end)
        ##- @oglobo
        oglobo   = pd.DataFrame(pyguana.Iguana.get(token=token,datainicio = start,datafim = end,fonte = "@oglobo"))['noticia']
        oglobo = pyguana.leitor(oglobo,start_date = start,end_date=end)
        ##- @zerohora
        zerohora = pd.DataFrame(pyguana.Iguana.get(token=token,datainicio = start,datafim = end,fonte = "zehora"))['noticia']
        zerohora = pyguana.leitor(zerohora,start_date = start,end_date=end)
        
        return valor_online


token = 'k2rt3f5'
