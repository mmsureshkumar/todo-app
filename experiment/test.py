from modules.functions import get_todos, write_todos
import time

# import functions

text = """
Mastering python
Good support for python
we can do anything on python
"""
print(text)

while True:
    user_action = input("Type as as add, show, edit, complete or Exit :")
    user_action = user_action.strip()
    if user_action.startswith("add"):
        todo = user_action[4:]
        lst = get_todos(filepath='../files/todos.txt')
        lst.append(todo + "\n")
        write_todos(filepath='../files/todos.txt', lst_local=lst)
    elif user_action.startswith("show"):
        lst = get_todos('../files/todos.txt')
        for index, item in enumerate(lst):
            print(f"{index} - {item}")
    elif user_action.startswith("edit"):
        # case "edit":
        number = int(input("Enter the number to edit : "))
        number = number - 1
        lst = get_todos(filepath='../files/todos.txt')
        new_todo = input("Enter new name : ")
        lst[number] = new_todo + "\n"
        write_todos(filepath='../files/todos.txt', lst_local=lst)
    elif user_action.startswith("complete"):
        # case "complete":
        number1 = int(input("Enter the number of todos to complete : "))
        lst = get_todos(filepath='../files/todos.txt')
        index = number1 - 1
        todos_to_remove = lst[index].strip('\n')
        lst.pop(number1)
        write_todos(filepath='../files/todos.txt', lst_local=lst)
        message = f"Todos: {todos_to_remove} was removed from the list of todos"
        print(message)
    else:
        # case "exit":
        break

print("Bye bye!!!")
