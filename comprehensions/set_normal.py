phrases = ["hello", "world", "python"]
set_data_normal = set()

for phrase in phrases:
    for char in phrase:
        set_data_normal.add(char.lower())


print(set_data_normal)
