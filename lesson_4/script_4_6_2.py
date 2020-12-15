from itertools import cycle


# б) итератор, повторяющий элементы некоторого списка, определенного заранее


def povtorelspiska(x,y):
    i = 0

    for el in cycle(x):
        if i > y-1:
            break
        else:
            print(el)
            i += 1
