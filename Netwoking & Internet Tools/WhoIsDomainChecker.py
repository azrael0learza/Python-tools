import whois
import PySimpleGUI as sg
from pprint import pprint

sg.theme('DarkBlue2')
layout = [[sg.Text("Enter Domain")],
          [sg.Text('Who Is') ,sg.InputText()],
          [sg.Text(size=(40,1), key='-OUTPUT-')],
          [sg.Button('Find'), sg.Button('Quit')]]

window = sg.Window('Who Is Domain Info', layout)

while True:  
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    
    domain_name = values[0]
    whois_info = whois.whois(domain_name)
  
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    
    sg.Print('Result', do_not_reroute_stdout=False)
    pprint(whois_info)

window.close()