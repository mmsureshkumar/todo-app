import FreeSimpleGUI as sg

label1 = sg.Text("Enter Feet:")
input1 = sg.Input()

label2 = sg.Text("Enter inches:")
input2 = sg.Input()

convert_button = sg.Button(auto_size_button=True)

window = sg.Window("Converter",[[label1, input1], [label2,input2], [convert_button]], auto_size_text=True)
window.read()
window.close()

