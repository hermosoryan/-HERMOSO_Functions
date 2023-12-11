print("Name: Hermoso Ryan")
print("Section: BS COMPUTER SCIENCE 1E")
print("Instructor: Mr. Ralph Angelo Baguio")
print("DATE: December 8, 2023")

def smallest_factor(n):
    if n < 2:
        print("Invalid input. Enter a number greater than or equal to 2.")
        return

    for i in range(2, n + 1):
        if n % i == 0:
            print(f"The smallest factor of {n} (other than 1) is: {i}")
            break

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_in_range(start, end):
    print(f"Prime numbers in the range [{start}, {end}]:")
    for number in range(start, end + 1):
        if is_prime(number):
            print(number)

# Example usage:
while True:
    print("\nSelect an option:")
    print("1. Find the smallest factor of a number.")
    print("2. Find prime numbers in a range.")
    print("3. Exit")

    try:
        choice = int(input("Enter your choice (1, 2, or 3): "))

        if choice == 1:
            number = int(input("Enter an integer greater than or equal to 2: "))
            smallest_factor(number)
        elif choice == 2:
            start_range = int(input("Enter the start of the range: "))
            end_range = int(input("Enter the end of the range: "))
            find_primes_in_range(start_range, end_range)
        elif choice == 3:
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

    except ValueError:
        print("Invalid input. Please enter a valid integer.")

