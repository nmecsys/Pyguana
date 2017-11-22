#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 18:02:58 2017

@author: fteixeira
"""

from Pyguana import iguana_get
import pandas as pd
from Pyguana import leitor


def iguana_reader(token, start, end, cenario = [1,2,3])
    
    assert(token is not None), "É preciso inserir um token válido! \n Solicite em www.iguana.incertezalab.com/documentation/index.php"
    assert(start or end is None), "É necessario passar a janela de data das notícias!" 
    
    ##- valor online
    valor_online = pd.DataFrame(iguana_get(token=token,datainicio = start,datafim = end,fonte = "Valor_Economico"))['noticia']
    leitor_valor_online = leitor(valor_online, start_date=start,end_date=end)
    
    ##- valor impresso    
    valor_impresso = pd.DataFrame(iguana_get(token=token,datainicio = "2012",datafim = "2015",fonte = "Valor_impresso"))['noticia']
    valor_impresso = leitor(valor_impresso,start_date = start,end_date=end)
    ##- folha online
    folha_online = pd.DataFrame(iguana_get(token=token,datainicio = start,datafim = end,fonte = "Folha_online"))['noticia']
    folha_online = leitor(folha_online,start_date = start,end_date=end)
    ##- folha impresso
    folha_impresso = pd.DataFrame(iguana_get(token=token,datainicio = start,datafim = end,fonte = "Folha_impresso"))['noticia']
    folha_impresso = leitor(folha_impresso,start_date = start,end_date=end)
    ##- @estadao
    estadao  = pd.DataFrame(iguana_get(token=token,datainicio = start,datafim = end,fonte = "@estadao"))['noticia']
    estadao = leitor(estadao,start_date = start,end_date=end)
    ##- @correio
    correio  = pd.DataFrame(iguana_get(token=token,datainicio = start,datafim = end,fonte = "@correio"))['noticia']
    correio = leitor(correio,start_date = start,end_date=end)
    ##- @oglobo
    oglobo   = pd.DataFrame(iguana_get(token=token,datainicio = start,datafim = end,fonte = "@oglobo"))['noticia']
    oglobo = leitor(oglobo,start_date = start,end_date=end)
    ##- @zerohora
    zerohora = pd.DataFrame(iguana_get(token=token,datainicio = start,datafim = end,fonte = "zehora"))['noticia']
    zerohora = leitor(zerohora,start_date = start,end_date=end)
    



