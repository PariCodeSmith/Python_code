def add_numbers(num1, num2):
  
    return num1 + num2

# 2. Get input from the user (converted to float to handle decimals)
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

# 3. Call the function and store the result
result = add_numbers(first_number, second_number)

# 4. Display the output
print(f"The sum of {first_number} and {second_number} is {result}")