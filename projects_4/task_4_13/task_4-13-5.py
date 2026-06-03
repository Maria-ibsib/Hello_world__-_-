N = int(input("Введите количество чисел: "))

i = 1
a = float(input("Введите число: "))
max_value = a

i = i + 1

while i <= N:
    a = float(input("Введите число: "))
    if a > max_value:
        max_value = a
    i = i + 1

print(max_value)