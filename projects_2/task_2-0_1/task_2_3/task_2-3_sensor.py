
operator_name = input("Введите имя оператора: ")
pressure_value = input("Введите текущее значение давления (Па): ")


with open("sensor_log.txt", "a", encoding="utf-8") as file:

    log_line = f"{operator_name}\t{pressure_value}"
    file.write(log_line + "\n")

print("Данные успешно сохранены в sensor_log.txt")