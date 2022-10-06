import json

def retrive_sample_data():
    file = open("sample4.json", "r")
    result = json.load(file)
    return result


def dump_dict_to_json(my_data):
    dumped_data = json.dump(my_data)
    file = open("my_dumped_data.json", "w")
    file.write(dumped_data)
    file.close()

