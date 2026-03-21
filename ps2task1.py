import random


def load_words():
    print("загрузка слов...")
    with open('words.txt', 'r', encoding="utf-8") as f:
        #открываем файл используя кодировку utf-8
        word = f.read().split()
    print("Загружено слов:", len(word))
    return word

def choose_word(wordlist):
    random_words = random.choice(wordlist)
    return random_words
    # возвращаем слово из списка обратно

def get_guessed_word(secret_word, guessed_letters):
    rez_line = ""
    for letter in secret_word:
        if letter in guessed_letters:
            rez_line += letter
            continue
        else:
            rez_line += '_'
    return rez_line




wordlist = load_words()
secret_word = choose_word(wordlist)



guessed_letters = []
attempts_left = 6

print(len(secret_word))

def in_word_guessed(secret_word, guessed_letters):
    for letter in secret_word:
        if letter not in guessed_letters:
            return False
    return True

while attempts_left > 0:
    print("Попыток осталось: ", attempts_left)
    letter = input("Введите слово:")
    letter = letter.lower()
    if len(letter) != 1 or not letter.isalpha():
        print("Введите одну букву")
        continue
    if letter in guessed_letters:
        print("Вы вводили такую букву!")
        continue
    else:
        guessed_letters.append(letter)
        if letter in secret_word:
            print("Вы угадали букву!")
        else:
            print("Вы не угадали букву!")
            attempts_left -= 1

        current_word = get_guessed_word(secret_word, guessed_letters)
        print(current_word)
        if in_word_guessed(secret_word, guessed_letters):
            print("Вы угадали слово")
            break

if attempts_left == 0:
    print("Вы проиграли")
    print("Слово было:", secret_word)






