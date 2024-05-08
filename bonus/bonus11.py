def get_averages():
    with open('../files/average.txt', 'r') as file:
        value = file.readlines()[1:]
    value = [float(i) for i in value]
    value = sum(value) / len(value)
    return value


def get_maximum():
    celsius1 = [14, 15.1, 12.3]
    maximum = max(celsius1)
    print(maximum)
    return float(maximum)


celsius = get_maximum()
fahrenheit = celsius * 1.8 + 32
print(fahrenheit)

average = get_averages()
print(average)
