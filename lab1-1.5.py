try:
    # Ввод ребра
    edge_length = int(input('Введите длину ребра куба: '))
    # Вычислить объем куба
    volume = edge_length ** 3
    # Вычислить площадь полной поверхности куба
    area = 6 * edge_length ** 2
   # Вывод результата
    print(f"Volume= {volume} \n Total surface area = {area}")
except ValueError:
    print("Ошибка: Введено нечисловое значение.")