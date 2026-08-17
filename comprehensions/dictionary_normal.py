names = ["randhir", "mohan", "akash", "sohan", "ahaan"]
print("printing all names", names)

names_dict_normal = {}
print("creating names dictionary staring with a")
for name in names:
    if (name.startswith('a')):
        names_dict_normal[name] = len(name)

print("printing names dictionary starting with a")
print(names_dict_normal)
