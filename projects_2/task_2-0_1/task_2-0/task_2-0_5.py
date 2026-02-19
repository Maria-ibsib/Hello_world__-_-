
name = "Иван Иванов"
group = "ПИ-23"
score = 85


with open("output.txt", "w", encoding="utf-8") as file:

    print(f"Студент {name} из группы {group} получил {score} баллов.", file=file)
