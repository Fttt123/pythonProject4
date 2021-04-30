_mas = []
def push(x):
    '''Добовление элемента в стек'''
    _mas.append(x)
    
def pop():
    '''Вернуть последний элемент стека'''
    return _mas.pop()

def clear():
    '''Очищает стек'''
    _mas.clear()

def is_empty():
    '''Проверка пустой-ли стек'''
    return len(_mas) == 0

def count():
    '''Возвращает количество элементов стека'''
    return len(_mas)
