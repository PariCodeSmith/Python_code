def is_palindrome_math(num):
    # Negative numbers cannot be palindromes
    if num < 0:
        return False
        
    original = num
    reversed_num = 0
    
    while num > 0:
        digit = num % 10                # Extract the last digit
        reversed_num = (reversed_num * 10) + digit  # Build the reversed number
        num = num // 10                 # Remove the last digit
        
    return original == reversed_num

# Example usage:
print(is_palindrome_math(121))   # Returns: True
print(is_palindrome_math(-121))  # Returns: False
