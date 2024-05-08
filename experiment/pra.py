user_prompt = "Enter the user name: "
lst = []
while True:
    todo = input(user_prompt)
    print(todo.capitalize())
    lst.append(todo.capitalize())
    print(lst)
