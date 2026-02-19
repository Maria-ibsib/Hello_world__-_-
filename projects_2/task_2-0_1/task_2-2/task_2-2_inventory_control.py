
reagent_name = input("Введите название реактива: ")
reagent_quantity = int(input("Введите количество (целое число): "))


report_line = f"Реактив {reagent_name} поступил на склад в количестве {reagent_quantity} шт."


print(report_line)


with open("inventory.txt", "a", encoding="utf-8") as file:
    file.write(report_line + "\n")

