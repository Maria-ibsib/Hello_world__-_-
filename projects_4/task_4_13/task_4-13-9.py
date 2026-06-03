print("Программа для суммы нечетных чисел")

N = int(input("Введите количество чисел N: "))

if N <= 0:
    print("Ошибка: N должно быть больше 0")
else:
    summa = 0
    i = 1

    while i <= N:
        print(f"Введите число {i}:")
        x = int(input())

        if x % 2 != 0:
            summa = summa + x

        i = i + 1

    print(f"Сумма нечетных чисел: {summa}")