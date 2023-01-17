File = 'todo.txt'
def get_todos(filepath=File):
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos

def write_todos(todos,filepath=File):
    with open(filepath, 'w') as file:
        file.writelines(todos)