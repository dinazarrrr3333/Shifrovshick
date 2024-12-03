
messenge = input("Введите сообщение: ")
chipher = []
result = ""

alphabet_ru = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
alphabet_en = "abcdefghijklmnopqrstuvwxyz"
print(messenge.lower())
step = int(input("Введите шаг сдвига: "))
lang = (input("""Выберите язык: RU/EN
Select a language: RU/EN
                 """))
if lang == "RU":
    lang = alphabet_ru  
elif lang == "EN":
    lang = alphabet_en
else:
    lang = alphabet_ru
    print("Язык по умолчанию русский")
for symbol in messenge:
    index = lang.find(symbol) + step
    chipher.append(index)
print(chipher)
for index in chipher:
    letter = lang[index - step]
    result += letter
print(result)