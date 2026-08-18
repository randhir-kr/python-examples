# Dictionaries {key: value} Ordered (as of Python 3.7+), mutable, stores data in key-value pairs. Keys must be unique and immutable.

user = {

    "name": "Sham",
    "age": "40",
    "is_active": True
}

# accessing value by key
print(user["age"])

# adding new key-value pair
user["email"] = "test@abc.com"

print(user)
