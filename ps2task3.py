import random
import string


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

def is_word_guessed(secret_word, letters_guessed):
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True

def get_guessed_word(secret_word, letters_guessed):
    result = ""

    for letter in secret_word:
        if letter in letters_guessed:
            result += letter + " "
        else:
            result += "_ "

    return result

def get_available_letters(letters_guessed):
    result = ""

    for letter in string.ascii_lowercase:
        if letter not in letters_guessed:
            result += letter

    return result




letter_guessed = []
wordlist = load_words()
secret_word = choose_word(wordlist)


guessed_letters = []
attempts_left = 6
warning_lefts = 3

print(len(secret_word))

def in_word_guessed(secret_word, guessed_letters):
    for letter in secret_word:
        if letter not in guessed_letters:
            return False
    return True

while attempts_left > 0:
    print("Попыток осталось: ", attempts_left)
    print("Доступные буквы: ", get_available_letters(guessed_letters))
    letter = input("Введите слово:")
    letter = letter.lower()
    if len(letter) != 1 or not letter.isalpha():
        print("Введите одну букву")
        continue
    if letter in guessed_letters:
        if  warning_lefts > 0:
            warning_lefts -= 1
            print("Вы уже вводили такую букву! Осталось предупреждений:", warning_lefts)
        else:
            attempts_left -= 1
            print("Вы уже вводили такую букву, вы теряете попытку")
            print(get_guessed_word(secret_word, guessed_letters))
            if is_word_guessed(secret_word, guessed_letters):
                print("Поздравляем, вы выиграли!")

                unique_letters = set(secret_word)
                score = attempts_left * len(unique_letters)

                print("Ваш счёт:", score)
                break
        continue
    else:
        guessed_letters.append(letter)
        if letter in secret_word:
            print("Вы угадали букву!")
        else:
            print("Вы не угадали букву!")

            if letter in "aeiou":
                attempts_left -= 2
            else:
                attempts_left -= 1

        current_word = get_guessed_word(secret_word, guessed_letters)
        print(current_word)
        if is_word_guessed(secret_word, guessed_letters):
            print("Вы выиграли")
            break


        if len(letter) != 1 or not letter.isalpha():
            if warning_lefts > 0:
                warning_lefts -= 1
                print("Это не буква! Осталось предупреждений: ", warning_lefts)
            else:
                attempts_left -= 1
                print("Это не буква, вы теряете попытку")
            continue

if attempts_left == 0:
    print("Вы проиграли")
    print("Слово было:", secret_word)






