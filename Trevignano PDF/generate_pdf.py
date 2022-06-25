# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 11:17:09 2017

@author: LukaszMalucha
"""





import pdfkit

css = 'custom-styles.css'

options = {
    'minimum-font-size': "16",
    'page-size':'A4',

}

pdfkit.from_file('2021.html', '2021_text.pdf', options=options, css=css)



