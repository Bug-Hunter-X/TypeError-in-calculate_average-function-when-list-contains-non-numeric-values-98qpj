def calculate_average(numbers):
    if not numbers:  # Handle empty list case
        return 0
    return sum(numbers) / len(numbers)

my_list = []
average = calculate_average(my_list)  # This will correctly return 0
print(average)  # Output: 0

my_list = [1, 2, 3, 4, 5]
average = calculate_average(my_list) 
print(average)  # Output: 3.0

my_list = [1, 2, 'a', 4, 5]
average = calculate_average(my_list) # This will throw TypeError
print(average)