# Function 1: Add numbers in a list
def add_numbers(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Function 2: Calculate the average of numbers in a list
def calculate_average(numbers):
    total = add_numbers(numbers)
    average = total / len(numbers)
    return average

# Function 3: Convert a list of strings to lowercase
def convert_to_lowercase(strings):
    lowercase_strings = []
    for string in strings:
        lowercase_strings.append(string.lower())
    return lowercase_strings

# Function 4: Check if a number is even
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

# Function 5: Find the maximum number in a list
def find_maximum(numbers):
    max_number = max(numbers)
    return max_number

# Function 6: Reverse a string
def reverse_string(string):
    reversed_string = string[::-1]
    return reversed_string

# Function 7: Count the occurrences of a character in a string
def count_occurrences(string, char):
    count = string.count(char)
    return count

# Function 8: Check if a string is a palindrome
def is_palindrome(string):
    reversed_string = reverse_string(string)
    if string == reversed_string:
        return True
    else:
        return False

# Function 9: Find the factorial of a number
def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)

# Function 10: Convert a list of numbers to strings
def convert_to_strings(numbers):
    strings = [str(num) for num in numbers]
    return strings

# Example usage of functions
numbers = [1, 2, 3, 4, 5]
strings = ["Hello", "World", "Python"]
number = 20
string = "Racecar"

print("Sum of numbers:", add_numbers(numbers))
print("Average of numbers:", calculate_average(numbers))
print("Lowercase strings:", convert_to_lowercase(strings))
print("Is", number, "even?", is_even(number))
print("Maximum number:", find_maximum(numbers))
print("Reverse of", string, ":", reverse_string(string))
print("Occurrences of 'l' in", string, ":", count_occurrences(string, 'l'))
print(string, "is a palindrome?", is_palindrome(string))
print("Factorial of", number, ":", factorial(number))
print("Strings from numbers list:", convert_to_strings(numbers))
