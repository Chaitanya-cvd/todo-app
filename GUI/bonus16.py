import FreeSimpleGUI as sg
label1 = sg.Text("Select files to compress")
input1 = sg.Input()
chose_button1 = sg.FilesBrowse("Choose")#button programmed to select files i.e the dot function

label2 = sg.Text("Select destination folder")
input2 = sg.Input()
chose_button2 = sg.FolderBrowse("Choose")#program built to browse the folder
compress_button = sg.Button("Compress")#used to create only a button widget on GUI

window = sg.Window("File Compressor",
                   layout=[[label1,input1,chose_button1],
                           [label2,input2,chose_button2],
                           [compress_button]]
                           )

#window is used for display purposes containing basic features of app like buttons and labels

window.read()
window.close()