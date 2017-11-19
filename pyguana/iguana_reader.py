#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 18:02:58 2017

@author: fteixeira
"""



def iguana_reader(token, start, end, cenario = [1,2,3])
    
    assert(token is not None), "É preciso inserir um token válido! \n Solicite em www.iguana.incertezalab.com/documentation/index.php"
    assert(start or end is None), "É necessario passar a janela de data das notícias!" 
    
    
'''
iguana.reader<-function(token,cenario = c(1,2,3),start,end){
   if(missing(token)){
      stop("Token nao detectado!")
      if(missing(start) & missing(end)){
        stop("E necessario passar a janela de data das noticias!")
      }else if(missing(end)){
        stop("Nao foi introduzido a data final das noticias!")
      }else if(missing(start)){
        stop("Nao foi introduzido a data inicial das noticias!")
      }
  }

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

