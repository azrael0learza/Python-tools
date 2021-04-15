#Import Section
import wikipedia
import wolframalpha
vclient = wolframalpha.Client('PJ2AEP-2L96XYT68W')
import PySimpleGUI

import PySimpleGUI as sg
  
  
# Choose a Theme for the Layout
sg.theme('DarkBlue2')
layout =[[sg.Text('Enter a Query'), sg.InputText()],[sg.Button('Search'), sg.Button('Cancel')]]
window = sg.Window('Search Assistant', layout)

  
# This is an Event Loop
while True:  
    event, values = window.read()
      
    if event in (None, 'Exit'):
        break
    if event == 'Search':

        answer= vclient.query(values[0])
        sg.popup(answer)
    
      
# Close
window.close()
#