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


def sortData(shapes):
    """
    Сортировка данных
    :param shapes: array, массив с данными
    :return: array, отсортированный массив
    """
    for i in range(1, len(shapes)):
        j = i-1
        if shapes[i][0][5:] > shapes[j+1][0][5:]:
            shapes[i], shapes[j+1] = shapes[j+1], shapes[j]
            j += 1
    return shapes


shape = readfromtxt('space.txt')
print(sortData(shape))
