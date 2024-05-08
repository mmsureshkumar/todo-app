def get_nr_items(items):
    result = items.split(",")
    return result


def calculate_time(h, g=9.80665):
    t = (2 * h / g) ** 0.5
    return t


time = calculate_time(100)
print(time)

res = get_nr_items("john,lisa,teresa")
print(res)
