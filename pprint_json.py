import json


def load_data(filepath):
    with open(filepath, encoding='utf-8') as data_file:
        json_content = json.loads(data_file.read())
    return json_content


def pretty_print_json(data):
    print(json.dumps(data, ensure_ascii=False, separators=(',', ':'), indent=2))


if __name__ == '__main__':
    while True:
        path = input('Укажите путь до json файла ')

        try:
            json_content = load_data(path)
            pretty_print_json(json_content)
            break
        except FileNotFoundError:
            print('Чё-то нет такого файла.')
        except json.decoder.JSONDecodeError:
            print('Прости, но это я не могу распарсить.')
