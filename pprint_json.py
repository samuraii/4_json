import json
import sys


def load_data(filepath):
    with open(filepath, encoding='utf-8') as data_file:
        data = json.loads(data_file.read())
    return data


def pretty_print_json(data):
    d = json.dumps(data, ensure_ascii=False,
                   separators=(',', ':'), indent=2)
    print(d)


if __name__ == '__main__':

        path_to_file = sys.argv[1]

        try:
            data = load_data(path_to_file)
            pretty_print_json(data)
        except FileNotFoundError:
            print('Чё-то нет такого файла.')
        except json.decoder.JSONDecodeError:
            print('Прости, но это я не могу распарсить.')
