#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 18:02:58 2017

@author: fteixeira
"""

from Pyguana import iguana_get


def iguana_reader(token, start, end, cenario = [1,2,3])
    
    assert(token is not None), "É preciso inserir um token válido! \n Solicite em www.iguana.incertezalab.com/documentation/index.php"
    assert(start or end is None), "É necessario passar a janela de data das notícias!" 
    
    ##- valor online
    valor_online = iguana_get(token=token,datainicio = start,datafim = end,fonte = "Valor_Economico")
    ##- valor impresso    
    valor_impresso = pd.DataFrame(iguana_get(token=token,datainicio = "2012",datafim = "2015",fonte = "Valor_impresso"))['noticia']
    ##- folha online
    folha_online = pd.DataFrame(iguana_get(token=token,datainicio = start,datafim = end,fonte = "Folha_online"))['noticia']
    ##- folha impresso
    folha_impresso = pd.DataFrame(iguana_get(token=token,datainicio = start,datafim = end,fonte = "Folha_impresso"))['noticia']
    ##- @estadao
    estadao  = pd.DataFrame(iguana_get(token=token,datainicio = start,datafim = end,fonte = "@estadao"))['noticia']
    ##- @correio
    correio  = pd.DataFrame(iguana_get(token=token,datainicio = start,datafim = end,fonte = "@correio"))['noticia']
    ##- @oglobo
    oglobo   = pd.DataFrame(iguana_get(token=token,datainicio = start,datafim = end,fonte = "@oglobo"))['noticia']
    ##- @zerohora
    zerohora = pd.DataFrame(iguana_get(token=token,datainicio = start,datafim = end,fonte = "zehora"))['noticia']
    
    
'''


  ##jornais
  ##- valor online
  valor_online = iguana.get(token=token,datainicio = start,datafim = end,fonte = "Valor_Economico")
  ##- valor impresso
  valor_impresso = iguana.get(token=token,datainicio = start,datafim = end,fonte = "Valor_impresso")$noticias
  ##- folha online
  folha_online = iguana.get(token=token,datainicio = start,datafim = end,fonte = "Folha_online")$noticias
  ##- folha impresso
  folha_impresso = iguana.get(token=token,datainicio = start,datafim = end,fonte = "Folha_impresso")$noticias
  ##- @estadao
  estadao  = iguana.get(token=token,datainicio = start,datafim = end,fonte = "@estadao")$noticias
  ##- @correio
  correio  = iguana.get(token=token,datainicio = start,datafim = end,fonte = "@correio")$noticias
  ##- @oglobo
  oglobo   = iguana.get(token=token,datainicio = start,datafim = end,fonte = "@oglobo")$noticias
  ##- @zerohora
  zerohora = iguana.get(token=token,datainicio = start,datafim = end,fonte = "zehora")$noticias

}


