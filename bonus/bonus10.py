try:
    width = float(input("Enter the width of the rectangle : "))
    length = float(input("Enter the length of the rectangle : "))

    if width == length:
        exit("That looks square")
    area = width * length
    print(area)
except ValueError:
    print("Please enter the number")
