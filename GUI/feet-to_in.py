import FreeSimpleGUI as sg

labeli = sg.Text("Enter feet:")
inputi = sg.Input()

labelii = sg.Text("Enter inches:")
inputii = sg.Input()
convert_button = sg.Button("Convert")

windows = sg.Window("Converter",
                    layout=[[labeli,inputi],
                            [labelii,inputii],
                            [convert_button]])


windows.read()
windows.close()
