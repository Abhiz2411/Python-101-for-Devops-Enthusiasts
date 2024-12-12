import json
with open('sample_data.json', 'r') as file:
    data = json.load(file)
    print(json.dumps(data, indent=4))