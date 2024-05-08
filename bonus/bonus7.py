user_prompt = input("Add a new Member : ")
file = open("../files/members.txt", "r")
lst = file.readlines()
file.close()

print(lst)

file = open("../files/members.txt", "w")
lst.append(user_prompt)
file.writelines(lst)
file.close()

filenames = ['doc.txt', 'report.txt', 'presentation.txt']
file_content = ["Hallo","fgdgsdfg","sfgdf"]
for name, content in zip(filenames, file_content):
    file = open(name,"w")
    file.writelines(content)
    file.close()

for name, content in zip(filenames, file_content):
    file = open(name,"r")
    print(file.readlines())
    file.close()