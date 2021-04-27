import base64
import PySimpleGUI as sg

encodeinput ='-INPUT-'

encoded = base64.b64encode(b'encodeinput')
# Define the window's contents
layout = [[sg.Text("What would you like to encode?")],
          [sg.Input(key=encodeinput)],
          [sg.Text(size=(40,1), key='-OUTPUT-')],
          [sg.Button('Ok'), sg.Button('Quit')]]

# Create the window
window = sg.Window('Window Title', layout)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break

    # Output a message to the window
    sg.popup((str(encoded[1: ])))
# Finish up by removing from the screen
window.close()


