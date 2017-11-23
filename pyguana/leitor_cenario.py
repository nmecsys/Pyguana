#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 18:02:23 2017

@author: fteixeira
"""


import io


def leitor(noticis, start_date, end_date, cenario):
    if cenario == 1:
        economic_words = ["ECONÔ", "ECONO", "-ECON", "MICROECON", "MACROECON", "SOCIOECON"]
        uncertainty_words = ["INCERT","INSTAB","CRISE"]
        politic_words = ["Govern", "Congress", "President", "Presidên","senado", "deput", "impeachment", "eleição"]
    elif cenario == 2:
        economic_words = ["ECONÔ", "ECONO", "-ECON", "MICROECON", "MACROECON", "SOCIOECON"]
        uncertainty_words ["INCERT","INSTAB","CRISE"]
        fiscal_words = ["Déficit", "superávit", "dívida", "fiscal", "orçament", "imposto", "dominância fiscal"]
    elif cenario == 3:
        economic_words = ["ECONÔ", "ECONO", "-ECON", "MICROECON", "MACROECON", "SOCIOECON"]
        uncertainty_words = ["INCERT","INSTAB","CRISE"]
        monetary_words = ["BCB", "BACEN","Selic", "Juros", "Copom", "Monet", "Infla","Banco Central"]
        
    
    
    cols=["id", "date", "n_encontrado", "n_total"]
    final_data = pd.read_csv(
        io.StringIO(""), 
        names=cols, 
        dtype=dict(zip(cols,[int, str, int, int])), 
        index_col=['id']
        )
    
    # Ver com Jonatha
    noticias = x[,2]
    datas = x[,1]
    
    for noticia in noticias:
        i = 0
        total = 0
        total_incerteza = 0

'''


 
  noticias = x[,2]
  datas = x[,1]
  for(i in 1:length(noticias)){
    total = 0
    total_incerteza = 0
    contador = 0
    contador = contador + 1
    total = total + 1

        fileName <- files[j]
        artigo <- readChar(noticias[i])
        artigo <- toupper(artigo)
        combina_termos = do.call(paste, expand.grid(economic_words,uncertainty_words))

        for(k in 1:length(combina_termos)){

          termo = unlist(strsplit(combina_termos[k]," "))

          resultado = all(str_detect(artigo,termo))

          if(resultado){
            total_incerteza = total_incerteza + 1
            break
          }

        }

      }

      new_row <- data.frame(
        date = data,
        n_encontrado = total_incerteza,
        n_total = total
      )

      final_data <- rbind(final_data,new_row)
      return(final_data)

}
