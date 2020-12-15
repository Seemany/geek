from itertools import count


# а) итератор, генерирующий целые числа, начиная с указанного

def ciklotdo(x, y):
    for el in count(x):
        if el > y:
            break
        else:
            print(el)
