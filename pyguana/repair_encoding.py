#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 18:03:48 2017

@author: fteixeira
"""


'''
repair_encoding=function (x, from = NULL)  {

    if (!requireNamespace("stringi", quietly = TRUE)) {
        stop("stringi package required for encoding operations")
    }
    if (is.null(from)) {

        best_guess <- guess_encoding(x)[1, , drop = FALSE]
        from <- best_guess$encoding
        conf <- best_guess$confidence * 100
        if (conf < 50) {
            stop()
        }
        #message("Best guess: ", from, " (", conf, "% confident)")
    }
    stringi::stri_conv(x, from = from)



}
