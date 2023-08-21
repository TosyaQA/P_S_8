#Напишите функцию, которая сереализует содержимое текущей директории в json-файл. В файле должен храниться список словарей, 
#словарь описывает элемент внутри директории: имя, расширение, тип. Если элемент - директория, то только тип и имя. 
#Пример результата для папки, где лежит файл test.txt и директория directory_test:
#[
#{
# 'name': 'test',
# 'extension': '.txt',
# 'type': 'file'
# },
# #{
# 'name': 'directory_test',
# 'type': 'directory',
# }
# ]

import os
import json

def serialize_directory():
    directory_items = []

    for item in os.scandir():
        print(item)
        item_info = {}
        item_info['name'] = item.name
        if item.is_file():
            item_info['extension'] = os.path.splitext(item.name)[1]
            item_info['type'] = 'file'
        elif item.is_dir():
            item_info['type'] = 'directory'
        directory_items.append(item_info)

    with open('directory.json', 'w') as file:
        json.dump(directory_items, file, indent=2)

serialize_directory()

# Результат
# [
#   {
#     "name": "Task.py",
#     "extension": ".py",
#     "type": "file"
#   }
# ]