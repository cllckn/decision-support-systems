import json

# JSON data with student records
data = {
    "students": [
        {"name": "John", "surname": "Doe", "age": 20, "address": "123 Main St, London, England"},
        {"name": "Alice", "surname": "Smith", "age": 22, "address": "456 Elm St, Paris, France"},
        {"name": "Bob", "surname": "Johnson", "age": 21, "address": "789 Oak St, New York, USA"}
    ]
}

# Accessing elements
print(data["students"][0]["name"])      # Output: John
print(data["students"][1]["age"])       # Output: 22
print(data["students"][2]["address"])   # Output: 789 Oak St, Chicago, USA


import json

# JSON data with student records and separate address records
data = {
    "students": [
        {
            "name": "John",
            "surname": "Doe",
            "age": 20,
            "address": {
                "street": "123 Main St",
                "city": "London",
                "country": "England"
            }
        },
        {
            "name": "Alice",
            "surname": "Smith",
            "age": 22,
            "address": {
                "street": "456 Elm St",
                "city": "Paris",
                "country": "France"
            }
        },
        {
            "name": "Bob",
            "surname": "Johnson",
            "age": 21,
            "address": {
                "street": "789 Oak St",
                "city": "New York",
                "country": "USA"
            }
        }
    ]
}

# Accessing elements
print(data["students"][0]["name"])              # Output: John
print(data["students"][1]["age"])               # Output: 22
print(data["students"][2]["address"]["city"])   # Output: Chicago
print(data["students"][0]["address"]["street"]) # Output: 123 Main St
