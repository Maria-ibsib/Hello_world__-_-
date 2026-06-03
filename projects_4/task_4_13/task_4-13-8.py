print("Программа для подсчета положительных чисел")

N = int(input("Введите количество чисел N: "))

if N <= 0:
    print("Ошибка: N должно быть больше 0")
else:
    count = 0
    i = 1

    while i <= N:
        print(f"Введите число {i}:")
        x = float(input())

        if x > 0:
            count = count + 1

        i = i + 1

    print(f"Количество положительных чисел: {count}")