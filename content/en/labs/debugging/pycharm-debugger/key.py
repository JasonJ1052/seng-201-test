def find_largest(numbers):
    largest = numbers[0]
    for i in range(1, len(numbers) + 1):  # Bug: should be range(1, len(numbers))
        if numbers[i] > largest:  # Bug: IndexError due to incorrect range in the loop
            largest = numbers[i]
    return largest

def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)  # Bug: Division by zero if list is empty
    return average

def main():
    numbers = [2, 8, 1, 6, 3, 12, 5, 9]

    print("Numbers:", numbers)

    largest_number = find_largest(numbers)
    print(f"The largest number is: {largest_number}")

    average_number = calculate_average(numbers)
    print(f"The average is: {average_number}")

    # Bug: Intentional logic error for students to find
    if largest_number < average_number:
        print("Something is wrong! The largest number is smaller than the average.")
    else:
        print("All calculations are correct.")

if __name__ == "__main__":
    main()
