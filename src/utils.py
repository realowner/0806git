
def item_exists(list_: list, index: int) -> str:
    if index > len(list_):
        return 'Вышли за пределы списка'
    return f'Ваш элемент: {list_[index]}'


if __name__ == '__main__':
    print(item_exists([1, 2], 1))
