# Напишите скрипт, который читает текстовый файл и выводит символы
# в порядке убывания частоты встречаемости в тексте. Регистр символа
# не имеет значения. Программа должна учитывать только буквенные
# символы (символы пунктуации, цифры и служебные символы слудет
# игнорировать). Проверьте работу скрипта на нескольких файлах с
# текстом на английском и русском языках, сравните результаты с
# таблицами, приведенными в wikipedia.org/wiki/Letter_frequencies.
def func(path):
    forbidden = '!@#№$%^&*( ),.:;?/|"[]+_-'
    try:
        with open(path, "r") as file:
            content = file.read().lower()  # чтение всего файла и приведение текста к нижнему регистру
            print("Текст из файла:", content)
            letters = dict()  # словарь для хранения букв(ключ) и количества их повторений(значение)
            for l in content:
                if l.isdigit() or l in forbidden:
                    continue
                else:
                    if l in letters:
                        letters[l] += 1
                    else:
                        letters[l] = 1
        list_d = list(letters.items())
        list_d.sort(key=lambda i: i[1], reverse=True)
        for i in list_d:
            print(i[0], ':', i[1])
    except IOError as error:
        print(error)


func("EngText.txt")
func("RusText.txt")
