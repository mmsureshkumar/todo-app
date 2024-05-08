import glob

files = glob.glob("files/*.txt")

for file in files:
    with open(file, 'r') as f:
        print(f.read())
