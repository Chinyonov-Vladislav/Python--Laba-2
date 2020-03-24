#Задан путь к директории с музыкальными файлами (в названии
#которых нет номеров, а только названия песен) и текстовый файл,
#хранящий полный список песен с номерами и названиями в виде строк
#формата «01. Freefall [6:12]». Напишите скрипт, который корректирует
#имена файлов в директории на основе текста списка песен.
import os
import glob
directory = "E:/python/лаба 2/Music/"
path = "E:/python/лаба 2/Music/music.txt"
os.chdir(directory) # переход в рабочую директорию
name_files_from_directory_without_extension =[name_file.replace(".mp3","") for name_file in glob.glob("*.mp3")] # возврат листа файлов с расширение .mp3 и удаление /n на конце строки
print(name_files_from_directory_without_extension)
try:
    with open(path, "r") as file:
        name_files_from_txt =[name_file.rstrip() for name_file in list(file.readlines())]
        file.close()
        for new_name in name_files_from_txt:
            for old_name in name_files_from_directory_without_extension:
                if old_name in new_name:
                    os.rename(old_name+".mp3",new_name)
                    print("Файл {0} переименован в {1}".format(old_name, new_name))
                    break
                else:
                    continue
except IOError as error:
    print(error)


