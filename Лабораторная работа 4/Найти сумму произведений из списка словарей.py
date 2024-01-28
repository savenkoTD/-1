import json
FILENAME = "input.json"

def task() -> float:
    with open(FILENAME) as f:
        data = json.load(f)
    total = 0
    for d in data:
        product = d['score'] * d['weight']
        total += product
    return round(total, 3)

print(task())
