numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result_normal = []
print(numbers_list)
print("Normal way of creating a list:")
even_numbers = []
print(even_numbers)

for number in numbers_list:
    if number % 2 == 0:
        print(f"number {number} is even")
        even_numbers.append(number)
        # result_normal.append(number*number)
        result_normal.append(number ** 2)

print(f"printing even numbers list : ", even_numbers)
print(f"normal list after modifying: ", result_normal)
