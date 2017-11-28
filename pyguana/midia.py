# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 14:00:35 2017

@author: fernando.teixeira
"""




def midia(ano, mes):
    
    '''
        A função get permite que se faça uma requisição à API Iguana, desde que possuindo um token
        válido, escolhendo todos os parâmetros que se deseja. Pode-se escolher a 'fonte' da notícia,
        ou seja, o jornal; é também possível delimitar uma data de início de uma de fim para o retorno
        das notícias e de que maneira ela foi categorizada pelo próprio jornal (em qual caderno a mesma
        se encontra). Exemplos de categoria seriam 'política', 'economia' ou 'esportes'.
        
    '''
    
    ## Lendo as séries históricas de mídia
    ## colocar a série histórica no banco de dados
    
    data_arquivo = 1
    total = 2
    incert = 3
    
    ## Valor Econômico online
