from googletrans import Translator
from pprint import pprint
import PySimpleGUI as sg



sg.theme('DarkBlue2')
layout = [[sg.Text("Enter Text")],
          [sg.Text('Translate this :') ,sg.InputText()],
          [sg.Text(size=(40,1), key='-OUTPUT-')],
          [sg.Button('Translate'), sg.Button('Quit')]]

window = sg.Window('Basic Py Translator', layout)


while True:  
        event, values = window.read()
        if event in (None, 'Exit'):
            break
    
        iniTran = values[0]
        translator = Translator()

        finTran = translator.translate(iniTran, dest='es')

        if event == sg.WINDOW_CLOSED or event == 'Quit':
            break
    
        sg.Print(do_not_reroute_stdout=False)
        pprint('Detected language: ' + finTran.src)
    
        pprint('-----------------------------------------------------------------------------')
        
        pprint('Translated language: ' + finTran.dest)
        pprint(finTran.text)
        pprint(finTran.pronunciation)
        
        
window.close()

