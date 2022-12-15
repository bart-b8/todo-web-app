FILEPATH = r'todos.txt'

import os

if not os.path.exists(FILEPATH):
    with open(FILEPATH, 'w') as file:
        pass

def get_todos(filepath = FILEPATH):
    """ Return list with all todos. """
    with open(filepath, 'r') as file_local:
        # todos_local = file_local.readlines()
        todos_local = file_local.read().splitlines() #Removes \n from each line
    return todos_local

def write_todos(todos_arg, filepath = FILEPATH):
    """ Accepts lists of stirngs. All should end with '\n' 
    and writes it to the file given. 
    """
    todos_arg = [arg + '\n' for arg in todos_arg]
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

if __name__ == "__main__":
    with open("testtodos.txt", 'x') as file:
        testtodos = ['test1', 'test2']
        testtodos = [i+'\n' for i in testtodos]
        file.writelines(testtodos)
    todos = get_todos("testtodos.txt")
    print(todos)
    newtodo = 'test function'
    todos.append(newtodo)
    write_todos(todos, "testtodos.txt")
    os.remove("testtodos.txt")
