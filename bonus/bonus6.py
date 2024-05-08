elements = ['a', 'b', 'c']
print(elements[1])

elements = ['a', 'b', 'c']
elements[1] = 'x'
print(elements)

filenames = ['document', 'report', 'presentation']
for index, file in enumerate(filenames):
    print(f"{index}-{file.capitalize()}.txt")

ips = ['100.122.133.105', '100.122.133.111']
user_prompt = int(input("Enter the index of the IP you want: "))
for index, ip in enumerate(ips):
    if index == 0:
        print(f"You chose {ip}")
        break
    elif index == 1:
        print(f"You chose {ip}")
        break

menu = ["pasta", "pizza", "salad"]
user_choice = int(input("Enter the index of the item: "))
message = f"You chose {menu[user_choice]}."
print(message)

menu1 = ["pasta", "pizza", "salad"]
for i, j in enumerate(menu1):
    print(f"{i}.{j}")

menu2 = ["pasta", "pizza", "salad"]
for i, j in enumerate(menu2):
    print(f"{i}.{j}")

buttons = [('John', 'Sen', 'Morro'), ('Lin', 'Ajay', 'Filip')]
for first, second, third in buttons:
    print(first, second, third)