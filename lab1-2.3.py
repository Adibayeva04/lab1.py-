try:
    # Вводим общее число
    num=int(input())
    # определяем округленное число
    odd=(num+1)//2
    # вывод округленного числа
    print(odd)
except ValueError:
    print("Ошибка: Ввод данных неверный.")
