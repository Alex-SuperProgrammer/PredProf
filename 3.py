def readfromtxt(filename):
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


def findData(shapeFindName):
    """
    Поиск корабля в массиве
    :param shapeFindName: str, название корабля
    :return: -
    """
    for i in range(101):
        if shapeFindName == shape[i][0]:
            print(f'Корабль {shape[i][0]} был отправлен с планеты: {shape[i][1]} и его направление движения было: {shape[i][3]}')


shape = readfromtxt('space.txt')
shapeName = input()
while shapeName != 'stop':
    findData(shapeName)
    shapeName = input()
