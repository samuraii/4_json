import json


def load_data(filepath):
    with open(filepath, encoding='utf-8') as data_file:
        data = json.loads(data_file.read())
    return data


def pretty_print_json(data):
    print(json.dumps(data, ensure_ascii=False, separators=(',', ':'), indent=2))


if __name__ == '__main__':
    while True:
        path = input('Укажите путь до json файла ')

        try:
            data = load_data(path)
            pretty_print_json(data)
            break
        except FileNotFoundError:
            print('Чё-то нет такого файла.')
        except json.decoder.JSONDecodeError:
            print('Прости, но это я не могу распарсить.')
