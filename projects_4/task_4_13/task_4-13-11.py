print("Программа для среднего арифметического элементов на четных позициях")

N = int(input("Введите количество чисел N: "))

if N < 2:
    print("Ошибка: N должно быть больше или равно 2")
else:
    summa = 0
    i = 1
    count = 0

    while i <= N:
        print(f"Введите число {i}:")
        x = float(input())

        if i % 2 == 0:
            summa = summa + x
            count = count + 1

        i = i + 1

    if count > 0:
        avg = summa / count
        print(f"Среднее арифметическое элементов на четных позициях: {avg}")
    else:
        print("Нет элементов на четных позициях")