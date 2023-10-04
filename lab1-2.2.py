#
try:
    # Ввод четерехзначных чисел
    num = int(input())
    # Вывод результатов
    print("The digit in the thousands position is",  num [0])
    print("The number in the hundreds position is", num[1])
    print("The digit in the tens position is", num[2])
    print("The digit in the tens position is", num[3])
except ValueError:
    # код обрабатывает исключение,если введено нецелое число
    print("Ошибка: Ввод целое четырехзначное число.")
