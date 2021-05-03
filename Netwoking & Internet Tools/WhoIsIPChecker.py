import PySimpleGUI as sg
from ipwhois import IPWhois
from ipwhois.net import Net
from ipwhois.asn import ASNOrigin
from pprint import pprint

sg.theme('DarkBlue2')
layout = [[sg.Text("Enter IP Address")],
          [sg.Text('Who Is') ,sg.InputText()],
          [sg.Text(size=(40,1), key='-OUTPUT-')],
          [sg.Button('Find'), sg.Button('Quit')]]

window = sg.Window('Who Is IP Finder', layout)


while True:  
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    
    net = Net(values[0])
    obj = ASNOrigin(net)
    iplook = obj.lookup(asn='AS37578')
    res = iplook

    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    
    sg.Print('Result', do_not_reroute_stdout=False)
    pprint(res)

    #sg.popup_scrolled(res)

window.close()



