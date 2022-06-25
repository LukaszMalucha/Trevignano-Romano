# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 11:17:09 2017

@author: LukaszMalucha
"""





import pdfkit

css = 'custom-styles.css'

options = {
    'minimum-font-size': "18",
    'page-size':'A4',

}

pdfkit.from_file('2016.html', '2016_text.pdf', options=options, css=css)



