donor = input("Введите группу крови донора (I, II, III, IV): ").strip().upper()
recipient = input("Введите группу крови пациента (реципиента) (I, II, III, IV): ").strip().upper()

valid_groups = {"I", "II", "III", "IV"}
if donor not in valid_groups or recipient not in valid_groups:
    print("Ошибка: введены некорректные группы крови. Используйте I, II, III или IV.")
else:
    if donor == "I" or donor == recipient:
        print("Переливание возможно.")
    else:
        print("Переливание невозможно.")