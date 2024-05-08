def get_todos(filepath):
    """Read a text file and return the list of items of todos"""
    with open(filepath) as file_local:
        lst_local = file_local.readlines()
    return lst_local


def write_todos(filepath, lst_local):
    """Write todo items to the list"""
    with open(filepath, 'w') as file_local:
        file_local.writelines(lst_local)