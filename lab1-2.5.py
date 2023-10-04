try:
    #Ввод двух чисел
    num1 = float(input("Ввод первого число: "))
    num2 = float(input("Ввод второго число: "))
    #Ввод выбора операции
    operation = input("Выберите операцию (+, -, *, /): ")
    #Переменная для хранения результата
    result=None
    # Проверка выбора операции и выполнение операции
    if operation == "+":
      result = num1 + num2
    elif operation == "-":
      result = num1 - num2
    elif operation == "*":
      result = num1 * num2
    elif operation == "/":
      if num2 == 0:
        print("Ошибка: Деление на ноль.")
      else:
        result = num1 / num2
    else:
        print("Ошибка: Неверный выбор операции.")

   # Вывод результата, если операция была выполнена успешно
    if result is not None:
       print(f"Результат операции {operation}: {result}")
except ValueError:
# Обработка исключения, если введены нечисловые значения
    print("Ошибка: Введите корректные числа.")
except Exception as e:
# Обработка других исключений
    print(f"Ошибка: {str(e)}")