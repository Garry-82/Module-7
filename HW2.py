import io
from pprint import pprint
def custom_write(file_name, strings):
    string_position = {}
    n = 1  # счетчик строки
    file = open(file_name, mode='a', encoding='utf-8')
    if len(strings) != 0:
        for i in strings:
            string_position[(n,  file.tell())] = i
            file.write(i+'\n')
            n += 1
    file.close()
    return string_position
#    print(file)
#    print(string_position)

info = ['Первая строка', 'Вторая строка', "dfsdfsdfs"]
result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)


