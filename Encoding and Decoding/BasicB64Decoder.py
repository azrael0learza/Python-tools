import base64
import PySimpleGUI as sg


layout = [[sg.Text("Enter Encoded Message")],
          [sg.Text('Decode') ,sg.InputText()],
          [sg.Text(size=(40,1), key='-OUTPUT-')],
          [sg.Button('Decode'), sg.Button('Quit')]]
 

window = sg.Window('Base64 Decoder', layout)


while True:  
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    
    #deco = (values[0])
    #decoded = (b64decode(deco))
    #(b64decode(deco).decode('utf-8'))

    deco = values[0]
    oced = deco.encode("ascii")

    decoded = base64.b64decode(oced)
    res = decoded.decode("ascii")

    
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    
    sg.popup_scrolled(decoded)


window.close()