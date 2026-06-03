print("Программа для вычисления среднего арифметического")

N = int(input("Введите количество чисел N: "))

if N <= 0:
    print("Ошибка: N должно быть больше 0")
else:
    summa = 0
    i = 1

    while i <= N:
        print(f"Введите число {i}:")
        x = float(input())
        summa = summa + x
        i = i + 1

    avg = summa / N
    print(f"Среднее арифметическое = {avg}")