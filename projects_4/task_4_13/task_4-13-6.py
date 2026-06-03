N = int(input("Введите число N: "))

sum_value = 0
i = 1

while i <= N:
    sum_value = sum_value + i**2
    i = i + 1

print(sum_value)