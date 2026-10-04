import json

data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}

with open("data_file.json", "w") as f:
    json.dump(data, f, indent=2)
# indent = using 2 spaces in formatting

with open("data_file.json", "r") as f:
    loaded = json.load(f)
print(loaded["president"]["name"])

jsonStr = json.dumps(data, indent=2)
print(jsonStr)

jsonString = """
{
    "researcher": {
        "name": "Ford Prefect",
        "species": "Betelgeusian",
        "relatives": [
            {
                "name": "Zaphod Beeblebrox",
                "species": "Betelgeusian"
            }
        ]
    }
}
"""

parsed = json.loads(jsonString)
for rel in parsed["researcher"]["relatives"]:
    print("Name: %s (%s)" % (rel["name"], rel["species"]))

demo = {
    "a_dict": {"key": "value"},
    "a_list": [1,2,3],
    "a_tuple_becomes_array": (4,5,6),
    "a_string": "hello",
    "a_int": 43,
    "a_float": 2.14,
    "a_bool_true": True,
    "a_bool_false": False,
    "a_none": None,
}
print(json.dumps(demo, indent=2))