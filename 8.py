import math

def is_prime(n):
    if n <= 1:
        return False
        
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False  
            
    return True  

try:
    user_input = int(input("Enter a positive integer to check: "))
    
    
    if is_prime(user_input):
        print(f"{user_input} is a prime number!")
    else:
        print(f"{user_input} is NOT a prime number.")
        
except ValueError:
    print("Invalid input! Please enter a valid integer.")
