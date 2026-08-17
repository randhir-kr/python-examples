phrases = ["hello", "world", "python"]

set_data_pythonic = {char.lower() for phrase in phrases for char in phrase}

print(set_data_pythonic)
