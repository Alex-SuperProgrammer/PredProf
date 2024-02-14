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


def generatePassword(shapes):
    """
    Генерация пароля
    :param shapes: array, массив кораблей
    :return: array, массив с генерироваными паролями
    """
    pas = []
    for i in range(1, 101):
        a = (shapes[i][1][5:] + shapes[i][0][1:3][::-1] + shapes[i][1][:3][::-1]).upper()
        pas.append(a)
    return pas


def writeToFile(name):
    """
    Запись данных в новый файл
    :param name: str, имя файла
    :return: -
    """
    with open(name, mode='w', encoding='UTF-8') as f:
        f.write(shape[0][0] + '*' + shape[0][1] + '*' + shape[0][2] + '*' + shape[0][3] + '*' + 'password' + '\n')
        for i in range(1, 99):
            f.write(shape[i][0] + '*' + shape[i][1] + '*' + shape[i][2] + '*' + shape[i][3] + '*' + code[i] + '\n')
    f.close()


shape = readFromTxt('space.txt')
code = generatePassword(shape)
writeToFile('space_uniq_password.csv')
