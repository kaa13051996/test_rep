import json
import requests
import random


class CreateObj:
    def __init__(self):
        self.id = random.randint(1, 10)
        self.name = f'ex#{random.randint(10, 20)}'
        self.test_list = [i for i in range(self.id, self.id * 5, self.id)]

    @staticmethod
    def run_up(objs):
        data = [{'id': obj.id, 'counter': obj.name, 'list': obj.test_list} for obj in objs]
        return data


def serialize(example=None):
    if example is None:
        data = {
            "president": {
                "name": "Zaphod Beeblebrox",
                "species": "Betelgeusian"
            }
        }
    else:
        data = json.dumps(example)

    final = json.dumps(data, sort_keys=True, indent=4)
    with open("data_file.json", "w") as file:
        json.dump(final, file)

    return final


def deserialize(download=False):
    if not download:
        with open("data_file.json", "r") as read_file:
            str_data = json.load(read_file)
            byte_data = json.loads(str_data)
    else:
        response = requests.get("https://jsonplaceholder.typicode.com/todos")
        byte_data = json.loads(response.text)

    return json.dumps(byte_data, sort_keys=True, indent=4)


if __name__ == '__main__':
    objs = [CreateObj() for i in range(10)]
    objs = CreateObj.run_up(objs)
    print(serialize(objs))
    temp = deserialize(False)
    print(temp)
