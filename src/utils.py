

def item_exists(list_: list, index: int) -> str:
    if index > len(list_):
        return 'Вышли за пределы списка'
    return f'Ваш элемент: {list_[index]}'

