# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 2017

@author: fernando.teixeira
"""


import pandas as pd
import requests
from pyguana import leitor


'''
    A classe `Iguana` é responsável por autorizar (ou não) o acesso do usuário à
    API de notícias Iguana. Para acessar qualquer função pertencente a esta classe
    exige-se primeiro o *input* de um token válido.
    
    A API Iguana é uma API de notícias criada pelo Núcleo de Métodos Estatísticos e
    Computacionais (NMEC) pertencente à FGV/IBRE cuja base é composta por algo em torno
    de 4 milhões de notícias dos principais jornais de diversas regiões do país.
    
    Ao efetuar uma requisição à API pode-se escolher a 'fonte' da notícia, ou seja, 
    o jornal; é também possível delimitar uma data de início de uma de fim para o retorno
    das notícias e de que maneira ela foi categorizada pelo próprio jornal (em qual 
    caderno a mesma se encontra). Exemplos de categoria seriam 'política', 'economia' ou 
    'esportes'.
    
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
               datafim=None, categoria=["Cotidiano", 
               "Educacao", "Esporte", "Poder", "Mundo", 
               "Ilustrada", "Mercado", "Ciencia", 
               "Equilibrio", "Turismo", "BBC Brasil", 
               "Tec", "Podcasts", "Veiculos", "Colunistas", 
               "Opiniao","Comida", "Imoveis", "Negocios",
               "Especial", "Equilibrio e Saude","Ambiente", 
               "Empregos", "Folha Corrida"], 
               limite=None):
    
        '''
        A função get permite que se faça uma requisição à API Iguana, desde que possuindo um token
        válido, escolhendo todos os parâmetros que se deseja. Pode-se escolher a 'fonte' da notícia,
        ou seja, o jornal; é também possível delimitar uma data de início de uma de fim para o retorno
        das notícias e de que maneira ela foi categorizada pelo próprio jornal (em qual caderno a mesma
        se encontra). Exemplos de categoria seriam 'política', 'economia' ou 'esportes'.
        
        '''
        
        url_base = 'http://iguana.incertezalab.com/jornais?token='
        
        assert(self.token is not None), ("É preciso inserir um token válido!" +
              "\n Solicite em www.iguana.incertezalab.com/documentation/index.php")
              
        if fonte is None and datainicio is None and datafim is None and categoria is None:
            dados = url_base + self.token
                
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
        dados = url_base + self.token + "".join([str(x) for x in params])
        dados_fin = requests.get(dados).json()

        if dados_fin['message'] == 'Token inválido':
            print ("É preciso inserir um token válido!" +
        "\nSolicite em www.iguana.incertezalab.com/documentation/index.php")
            return None
        elif dados_fin['message'] == 'Token nao encontrado!':
            print ("Você precisa inserir um token!" +
        "\nSolicite em www.iguana.incertezalab.com/documentation/index.php")
            return None
        
        dados_fin = pd.DataFrame(dados_fin['data'])    
        
 
        if dados_fin.empty == True:
                print ("Não há notícias com as especificações selecionadas.")
                return None

        
        return dados_fin


    
    
    def uncertainty_get(self, fonte=None, datainicio=None,
                           datafim=None, categoria=["Cotidiano", 
               "Educacao", "Esporte", "Poder", "Mundo", 
               "Ilustrada", "Mercado", "Ciencia", 
               "Equilibrio", "Turismo", "BBC Brasil", 
               "Tec", "Podcasts", "Veiculos", "Colunistas", 
               "Opiniao","Comida", "Imoveis", "Negocios",
               "Especial", "Equilibrio e Saude","Ambiente", 
               "Empregos", "Folha Corrida"], 
                           nmec=None):
                               
        '''
        A função uncertainty_get permite que se faça uma requisição à API Iguana 
        sobre as notícias relacionadas à incerteza mais especificamente. Esta função
        atua de forma complementar e similar à função `get`, para um fim mais específico.
        Novamente, ressalta-se que é obrigatório o uso de um token válido para se ter 
        acesso aos dados.
        
        '''  
        
    
        url_base = 'http://iguana.incertezalab.com/incerteza?token='
        
        assert(self.token is not None), ("É preciso inserir um token valido!" +
              "\n Solicite em www.iguana.incertezalab.com/documentation/index.php")
        
        if fonte is None and datainicio is None and datafim is None and categoria is None:
            dados = url_base + self.token
            dados_fin = requests.get(dados).json()
            
        return dados_fin['data']
    
    
    
    

    def reader(self, start, end, cenario = [1,2,3]):
        
        # start='2010-01-01'
        # end='2011-03-01'
    
        assert(self.token is not None), "É preciso inserir um token válido! \n Solicite em www.iguana.incertezalab.com/documentation/index.php"
        assert(start or end is None), "É necessario passar a janela de data das notícias!" 
        
        ##- valor online
        valor_online = Iguana.get(self, datainicio = start,datafim = end,fonte = "Valor_Economico")['noticia']
        valor_online = leitor(valor_online, start_date=start,end_date=end)
        
        ##- valor impresso    
        valor_impresso = Iguana.get(self.token,datainicio = "2012",datafim = "2015",fonte = "Valor_impresso")['noticia']
        valor_impresso = leitor(valor_impresso,start_date = start,end_date=end)
        ##- folha online
        folha_online = Iguana.get(self.token,datainicio = start,datafim = end,fonte = "Folha_online")['noticia']
        folha_online = leitor(folha_online,start_date = start,end_date=end)
        ##- folha impresso
        folha_impresso = Iguana.get(self.token,datainicio = start,datafim = end,fonte = "Folha_impresso")['noticia']
        folha_impresso = leitor(folha_impresso,start_date = start,end_date=end)
        ##- @estadao
        estadao  = Iguana.get(self.token,datainicio = start,datafim = end,fonte = "@estadao")['noticia']
        estadao = leitor(estadao,start_date = start,end_date=end)
        ##- @correio
        correio  = Iguana.get(self.token,datainicio = start,datafim = end,fonte = "@correio")['noticia']
        correio = leitor(correio,start_date = start,end_date=end)
        ##- @oglobo
        oglobo   = Iguana.get(self.token,datainicio = start,datafim = end,fonte = "@oglobo")['noticia']
        oglobo = leitor(oglobo,start_date = start,end_date=end)
        ##- @zerohora
        zerohora = Iguana.get(self.token,datainicio = start,datafim = end,fonte = "zehora")['noticia']
        zerohora = leitor(zerohora,start_date = start,end_date=end)
        
        return (valor_online, valor_impresso, folha_impresso, estadao, correio,
                oglobo, zerohora)



