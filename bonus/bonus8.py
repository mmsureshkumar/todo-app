new = [i*2 for i in ['a', 'b', 'c']]
print(new)

temperatures = ['10', '12', '14']
file = open("file.txt", 'w')
file.writelines(temperatures)