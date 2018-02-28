import json
import sys


def load_data(filepath):
    with open(filepath, encoding='utf-8') as data_file:
        data_from_file = json.loads(data_file.read())
    return data_from_file


def pretty_print_json(data_from_file):
    json_data = json.dumps(
            data_from_file, 
            ensure_ascii=False,
            separators=(',', ':'), 
            indent=2
    )
    
    print(json_data)


if __name__ == '__main__':
        path_to_file = sys.argv[1]

        try:
            data_from_file = load_data(path_to_file)
            pretty_print_json(data_from_file)
        except FileNotFoundError:
            print('Чё-то нет такого файла.')
        except json.decoder.JSONDecodeError:
            print('Прости, но это я не могу распарсить.')
