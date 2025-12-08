import random

def load_words():
    print("Loading word list from file...")
    with open("words.txt", "r") as file:
        wordlist = file.readline().split()
    print(f"{len(wordlist)} words loaded.")
    return wordlist

def choose_word(wordlist):
    return random.choice(wordlist)

wordlist = load_words()
secret_word = choose_word(wordlist)
print("Секретное слово:", secret_word)

attempts_left = 6

while attempts_left > 0:
    user_input = input(f"Попыток осталось: {attempts_left}. Введите букву: ")
    if len(user_input) != 1 or not user_input.isalpha():
        print("Введите только одну букву.")
        continue
    print("Вы ввели:", user_input)
    attempts_left -= 1

if attempts_left == 0:
    print("Вы исчерпали все попытки. Игра окончена.")

guessed_letters = []
guessed_letters.append(user_input)

if user_input in secret_word:
    print("Есть такая буква")
else:
    print("Такой буквы нет")
    attempts_left -= 1

guessed_letters = []

while True:
    # 1. Получи ввод от пользователя как строку
    letter = input("Введите букву: ").lower()

    # 2. Проверка корректности ввода
    if len(letter) != 1 or not letter.isalpha():# условие про 1 букву и isalpha
        print("Введите только одну букву")
        continue                    # здесь должен быть continue

    # 3. Проверка: вводилась ли буква раньше
    if letter in guessed_letters:
        print("Вы уже вводили такую букву!")
        continue                    # continue

    # 4. Добавляем новую букву
    print("Вы ввели новую букву:", letter)
    guessed_letters.append(letter)   # добавление буквы

    if letter in secret_word:
        print("Такая буква есть!")
    else:
        print("Такой буквы нет!")
        attempts_left -= 1

    def  in_word_guessed(secret_word, guessed_letters):
        print("Поздравляем! Вы угадали слово:", secret_word)

    if letter == 'q':
        break


def get_guessed_word(secret_word, guessed_letters):
    result = ""
    for letter in secret_word:
        if letter in guessed_letters:
            result += letter
        else: result += "_"

    return result
def in_word_guessed(secret_word, guessed_letters):
    return all(letter in guessed_letters for letter in secret_word)
