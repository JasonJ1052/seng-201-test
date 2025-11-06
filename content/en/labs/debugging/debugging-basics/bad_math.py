def find_largest(numbers):
    largest = numbers[0]
    for i in range(1, len(numbers) + 1):
        if numbers[i] > largest:
            largest = numbers[i]
    return largest

def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average

def main(numbers):
    print("Numbers:", numbers)

    largest_number = find_largest(numbers)
    print(f"The largest number is: {largest_number}")

    average_number = calculate_average(numbers)
    print(f"The average is: {average_number}")

    if average_number < largest_number:
        print("\u2705 All calculations are correct.")
    else:
        print("\u274c Something is wrong! The largest number is smaller than the average.")
    
    print('-'*8)

if __name__ == "__main__":
    main([2, 8, 1, 6, 3, 12, 5, 9])
    main([32, 16, 8, 4, 2, 1, 0])
    main([])
    main([2])
    main([12,12])
