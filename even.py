def find_largest(numbers):
    return max(numbers)
def find_smallest(numbers):
    return min(numbers)
def calculate_average(numbers):
    return sum(numbers) / len(numbers)
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
if __name__ == "__main__":
    numbers = [10, 25, 5, 40, 18]
    print("Numbers:", numbers)
    print("Largest number:", find_largest(numbers))
    print("Smallest number:", find_smallest(numbers))
    print("Average:", calculate_average(numbers))
    num = int(input("Enter a number to check even or odd: "))
    print("The number is:", check_even_odd(num))