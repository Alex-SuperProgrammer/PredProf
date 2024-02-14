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


def correct(shapes):
    """
    Исправление побитных данных
    :param shapes: array, массив кораблей
    :return: arry, исправленный массив кораблей
    """
    for i in range(1, 100):
        n = shapes[i][0][5:6]
        m = shapes[i][0][6:7]
        t = len(str(shapes[i][1]))


shape = readFromTxt('space.txt')
correct(shape)
