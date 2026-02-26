
sequence = input("Введите последовательность ДНК: ")
sequence_upper = sequence.upper()

count_a = sequence_upper.count('A')
count_t = sequence_upper.count('T')
count_g = sequence_upper.count('G')
count_c = sequence_upper.count('C')

total_length = len(sequence_upper)


if total_length > 0:
    percent_a = (count_a / total_length) * 100
    percent_t = (count_t / total_length) * 100
    percent_g = (count_g / total_length) * 100
    percent_c = (count_c / total_length) * 100
else:
    percent_a = percent_t = percent_g = percent_c = 0.0


print("\n=== Анализ последовательности ДНК ===\n")
print(f"Последовательность в верхнем регистре: {sequence_upper}\n")
print("Подсчёт нуклеотидов:")
print(f"A: {count_a}")
print(f"T: {count_t}")
print(f"G: {count_g}")
print(f"C: {count_c}\n")
print(f"Общая длина: {total_length} нуклеотидов\n")


print("Процентное содержание нуклеотидов:")
print(f"A: {percent_a:.2f}%")
print(f"T: {percent_t:.2f}%")
print(f"G: {percent_g:.2f}%")
print(f"C: {percent_c:.2f}%")