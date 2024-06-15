
def item_exists(list_: list, index: int) -> str:
    if index > len(list_):
        return 'Вышли за пределы списка'
    return f'Ваш элемент: {list_[index]}'


def func(my_str: str, count: int) -> str:
    if isinstance(count, int) and isinstance(my_str, str):
        return my_str * count
    raise TypeError('Ошибка типов')


if __name__ == '__main__':
    print(item_exists([1, 2], 1))
    print(func('hello', 3))
