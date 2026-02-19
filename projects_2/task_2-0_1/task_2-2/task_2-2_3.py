
device_name = "Термостат цифровой"
inventory_number = "TS‑0042"
is_working = True
quantity = 5


print("Название прибора\t\tИнвентарный номер\tСостояние\tКоличество")
print(f"{device_name}\t\t{inventory_number}\t\t{'Исправен' if is_working else 'Неисправен'}\t{quantity}")
