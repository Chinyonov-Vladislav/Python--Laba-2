# Напишите скрипт, позволяющий искать в заданной директории и в ее
# подпапках файлы-дубликаты на основе сравнения контрольных сумм
# (MD5). Файлы могут иметь одинаковое содержимое, но отличаться
# именами. Скрипт должен вывести группы имен обнаруженных файлов дубликатов.
#E:/python/лаба 2/dir
class DirectoryNotFindException(Exception):
   pass
import os
import hashlib
start_path =input("Введите начальную директорию: ")
paths_of_files = list()
checksum = list()
try:
    if os.path.isdir(start_path):
        tree = os.walk(start_path)
        for address, dirs, files in tree:
            for file in files:
                paths_of_files.append(address + "\\" + file)
    else:
        raise DirectoryNotFindException("Введенной директории не существует!")
    try:
        for path in paths_of_files:
            with open(path, "rb") as file:
                content = file.read()
                file.close()
                checksum.append(hashlib.md5(content).hexdigest())
        for i in range(len(checksum) - 1):
            for j in range(i + 1, len(checksum)):
                if checksum[i] == checksum[j]:
                    print(paths_of_files[j] + " is duplicate of " + paths_of_files[i])
    except IOError as err:
        print(err)
except DirectoryNotFindException as err:
    print(err)



