from src.utils import item_exists


def main():
    my_list = [123, 'Cat', -812, 'Ball', 'Q']
    user_input = input('index: ')
    if user_input.isdigit():
        ind = int(user_input)
        print(item_exists(my_list, ind))
    else:
        print('Введи не число(')


if __name__ == '__main__':
    main()
