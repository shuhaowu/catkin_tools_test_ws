import pkgutil

def get_message():
    return pkgutil.get_data('py_dummy_pkg', 'data/message.txt')
