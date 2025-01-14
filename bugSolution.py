def calculate_average(numbers):
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0
    return sum(numeric_numbers) / len(numeric_numbers)

my_list = []
average = calculate_average(my_list) 
print(average)  # Output: 0

my_list = [1, 2, 3, 4, 5]
average = calculate_average(my_list)
print(average)  # Output: 3.0

my_list = [1, 2, 'a', 4, 5]
average = calculate_average(my_list) # This will correctly return 3.0
print(average) # Output: 3.0