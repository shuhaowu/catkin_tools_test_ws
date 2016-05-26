#!/usr/bin/env python

from py_dummy_pkg import loader


def main():
    m = loader.get_message()
    print('The message is: {}'.format(m))
    return 0


if __name__ == '__main__':
    main()
