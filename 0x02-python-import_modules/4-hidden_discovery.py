#!/usr/bin/env python3

import hidden_4
import sys

if __name__ == '__main__':
    names = dir(hidden_4)
    for name in sorted(name):
        if not name.startswith('__'):
            print(name)
