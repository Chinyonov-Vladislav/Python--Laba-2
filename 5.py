#Введите с клавиатуры текст. Программно найдите в нем и выведите
#отдельно все слова, которые начинаются с большого латинского
#символа (от A до Z) и заканчиваются 2 или 4 цифрами, например
#«Petr93», «Johnny70», «Service2002». Используйте регулярные
#выражения.
# Пример текста: Vasya227872 nic0n0R Savenkov25 Shariy2000 Nemcov144 dibil2535 Petr93
import re
text =" " + input("Enter text:").replace("."," ").replace(",","").replace("!"," ").replace("?"," ").replace(":"," ").replace(":"," ").replace("-"," ")+ " "
print("Введенная строка:",text)
regex1 = re.compile('[A-Z]{1}[a-z,A-Z]*[0-9]{2}\s|[A-Z]{1}[a-z,A-Z]*[0-9]{4}\s')
result1= re.findall(regex1,text)
if len(result1)!=0:
    print("Результат: слова, начинающиеся с большой латинской буквы от A до Z и заканивающиеся 2 или 4 цифрами")
    for word in result1:
        print(str(word).strip())
else:
    print("Слов по шаблону не найдено")




