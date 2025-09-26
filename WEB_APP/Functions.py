# def read_todos():
#     with open('todolist.txt', 'r') as opening:
#         return opening.readlines()

import os

def read_todos():
    base_path = os.path.dirname(__file__)
    filepath = os.path.join(base_path, "todolist.txt")
    try:
        with open(filepath, "r") as opening:
            return opening.readlines()
    except FileNotFoundError:
        return []



def write_todos(todos):
    import os
    base_path = os.path.dirname(__file__)
    filepath = os.path.join(base_path, "todolist.txt")
    with open(filepath, "w") as file:
        file.writelines([todo.strip() + "\n" for todo in todos])



if __name__ == "__main__": print("Hello")