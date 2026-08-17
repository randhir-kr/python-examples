names = ["randhir", "mohan", "akash", "sohan", "ahaan"]
print("printing all names", names)

names_dict_pythonic = {}
print("creating names dictionary staring with a")
names_dict_pythonic = {
    name: len(name) for name in names if name.startswith('a')}

print("printing names dictionary starting with a")
print(names_dict_pythonic)
