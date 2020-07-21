#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    realn = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            realn += 1
        except ValueError:
            pass
        except IndexError as err:
            raise
        except TypeError:
            pass
    print()
    return realn
