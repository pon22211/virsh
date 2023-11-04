with open("1.txt", "r", encoding="utf-8")as file:
    for line in file:
        print(line)
author = input("Введіть автора")
with open("1.txt", "a", encording="utf-8") as file:
    file.write(author)
while True:
    answer = input("Додати нову цитату (Так/Ні):")
    if answer == "Так":
        quote = input("Додати цитату:")
        author = input("Введіть автора:")
        file = open("1.txt", "r", encoding="utf-8")as file:
        file.write(quote +"\n" + author)
        file.close()
    else:
        break
with open("1.txt", "r", encoding="utf-8")as file:
    for line in line:
        print(line)