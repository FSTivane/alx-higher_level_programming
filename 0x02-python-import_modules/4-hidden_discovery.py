#!/usr/bin/python3

import importlib.util


def print_names_from_pyc(pyc_file):
    spec = importlib.util.spec_from_file_location("hidden_4", pyc_file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    # Get names from the module excluding those starting with '__'
    names = [name for name in dir(module) if not name.startswith('__')]

    # Print the sorted names
    for name in sorted(names):
        print(name)


if __name__ == "__main__":
    print_names_from_pyc('hidden_4.pyc')
