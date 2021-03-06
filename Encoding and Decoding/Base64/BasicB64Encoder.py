import base64
import PySimpleGUI as sg


layout = [[sg.Text("Enter Text To Encode")],
          [sg.Text('Encode') ,sg.InputText()],
          [sg.Text(size=(40,1), key='-OUTPUT-')],
          [sg.Button('Encode'), sg.Button('Quit')]]
 

window = sg.Window('Base64 Encoder', layout)


while True:  
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    
    enco = values[0]
    encoded = base64.b64encode(enco.encode())

    
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    
    sg.popup_scrolled(encoded)

window.close()