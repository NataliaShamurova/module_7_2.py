
def custom_write(file_name, strings):
    strings_positions = {}  # Ключ - номер строки и байт начала строки (0, 0)
    with open(file_name, 'w', encoding='utf-8') as file:
        for string in strings:

            # Получаем текущую позицию в файле перед записью
            position = file.tell()

            # Записываем строку в файл с добавлением перевода строки
            file.writelines(string + '\n')

            # Добавляем в словарь позицию и строку
            strings_positions[(len(strings_positions) + 1, position)] = string


    return strings_positions



info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
