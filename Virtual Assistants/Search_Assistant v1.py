#Import Section
import wolframalpha
vclient = wolframalpha.Client('PJ2AEP-2L96XYT68W')

import wikipedia

import PySimpleGUI

import PySimpleGUI as sg
  
  
# Choose a Theme for the Layout
sg.theme('DarkBlue2')
layout =[[sg.Text('Enter a Query'), sg.InputText()],[sg.Button('Search')]]
window = sg.Window('Search Assistant', layout)

  
# This is an Event Loop
while True:  
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    
    answer= vclient.query(values[0])
    wolframres = next(answer.results).text
    wikires =  wikipedia.summary(values[0], sentences=1)
    sg.popup(wolframres or wikires)
    

# Close
window.close()
#

