feet_inches = input("Enter the feet and inches: ")


def parse(feet_inches1):
    parts = feet_inches1.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return {"feet": feet, "inches": inches}


def convert(feet, inches):
    meters = feet * 0.3408 + inches * 0.7468
    #print(f"feet {feet} and inches {inches} are equal to meters {meters}")
    return meters


parsed = parse(feet_inches)

result = convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} feet and {parsed['inches']} and the result {result}")

if result < 1:
    print("Kid is too small")
else:
    print("Kid can use the slide")
