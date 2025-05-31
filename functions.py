FILEPATH = "totos.txt"
def get_todos(filepath = FILEPATH):
    """" Reads a text file and returns the list of the to-do items."""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg,filepath = FILEPATH):
    """" Writes the to-do items list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)



print("Hello from functions")
