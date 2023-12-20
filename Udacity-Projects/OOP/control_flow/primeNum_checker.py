def is_prime(number):
    """
    Check if a given number is a prime number.
    
    Args:
        number (int): The number to be checked.
    
    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def print_prime_status(num):
    """
    Print whether a number is prime or not, and if not, print one of its factors.
    
    Args:
        num (int): The number to be checked.
    """
    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        for i in range(2, int(num/2) + 1):
            if num % i == 0:
                print(f"{num} is NOT a prime number, because {i} is a factor of {num}.")
                break

# List of numbers to check
# check_prime = [7, 26, 13, 10, 29]

# Check each number in the list
for num in range(2, 101):
    print_prime_status(num)
