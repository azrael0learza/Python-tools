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

        finTran1 = translator.translate(iniTran, dest='zh-cn')
        finTran2 = translator.translate(iniTran, dest='zh-tw')

        if event == sg.WINDOW_CLOSED or event == 'Quit':
            break
    
        sg.Print(do_not_reroute_stdout=False)
        print('Simplified')
        pprint('Detected language: ' + finTran1.src)
        pprint('Translated language: ' + finTran1.dest)
        pprint(finTran1.text)
        pprint(finTran1.pronunciation)
        pprint('-----------------------------------------------------------------------------')
        print('Traditional')
        pprint('Detected language: ' + finTran2.src)   
        pprint('Translated language: ' + finTran2.dest)
        pprint(finTran2.text)
        pprint(finTran2.pronunciation)
        
        
window.close()

