def readFromTxt(filename):
    """
    Чтение txt файла из запись в массив
    :param filename: str, имя файла
    :return: array, прочитанный файл в виде массива
    """
    shapes = []
    with open(filename, mode='r', encoding='UTF-8') as f:
        for i in range(101):
            shapes.append(f.readline().strip().split('*'))
        return shapes


def hash(shapes):
    """
    Создание хэш-таблицы для кораблей
    :param shapes: array, массив кораблей
    :return: -
    """
    for i in range(1, 11):
        print(f'{shapes[i][1]}:{shapes[i][0]}')


shape = readFromTxt('space.txt')
hash(shape)
