try:
    # Ввод четерехзначных чисел
    num=int(input())
    # Ввод каждоого числа
    thousands = (num % 10000) // 1000
    hundreds = (num % 1000) // 100
    tens = (num % 100) // 10
    onse = (num % 10)
    print(f"num1:{thousands}")
    print(f"num2 :{hundreds}")
    print(f"num3:{tens}")
    print(f"num4:{onse}")
except ValueError:
    print("ввод ошибки")

