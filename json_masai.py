import json
student = {
    "name": "John Doe",
    "age": 20,
    "marks": [85, 90, 78],
    "passed": True,
    "address": {
        "city": "Anytown",
        "pincode": "12345"
    }
}
json_data = json.dumps(student, indent=4)
print(json_data)

data  =  json.loads(json_data)
print(data["name"])
print(data["age"])
print(data["marks"])

bad_json = '{"name": "john", "age": 30, "city": "New York",}'
fixed_json = '{"name": "john", "age": 30, "city": "New York"}'

parsed = json.loads(fixed_json)
print(parsed)

products = [
    {"name": "Laptop", "price": 999.99, "quantity": 10},
    {"name": "Smartphone", "price": 499.99, "quantity": 20},
    {"name": "Headphones", "price": 199.99, "quantity": 15}
]

print(json.dumps(products, indent=4))
print(json.dumps(products, indent=4, sort_keys=True))