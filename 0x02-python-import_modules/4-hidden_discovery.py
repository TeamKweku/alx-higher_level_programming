#!/usr/bin/python3
if __name__ == "__main__":
    """ Print all names in hidden_4 module """
    import hidden_4

    builtin_names = dir(hidden_4)
    for name in builtin_names:
        if name[:2] != "__":
            print(name)
