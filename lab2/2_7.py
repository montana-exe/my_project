def count_vowels(text):
    vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

sentence = input("Введите текст: ")
print("Количество гласных букв:", count_vowels(sentence))
