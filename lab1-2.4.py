try:
    # вводим значение
    num1 = int(input("Enter the number: "))
    # бинарный сдвиг влево
    num2 = num1 << 1
    # сравниваем если число равно 0 выводим на экран предупреждение
    if num2 == 0:
        print("Warning! The result is zero!")
    # иначе выводим результат
    else:
        print(f"The result of << is {num2}")
except ValueError:
    print("Ввод данных неверный")