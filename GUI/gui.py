from re import match

import functions
import  FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo",key="todo")
add_button = sg.Button("Add")

window = sg.Window('My To-Do App',
                   layout=[[label],[input_box],[add_button]],
                   font=('Helvetica',20))
#font is a tuple and layout is a list
while True:
    event,values = window.read()#event gets value of add and values gets value of todos and input
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()
