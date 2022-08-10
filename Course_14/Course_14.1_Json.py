import pprint

import My_module

json_data = My_module.retrive_sample_data()
print(json_data)
print(type(json_data))
pprint.pp(json_data)

my_dict = {
    "name": "Razvan",
    "no" : 32,
    "something": True
}

My_module.dump_dict_to_json(my_dict)