def check_number(x):
    if x > 0:
        return "Positive"
    else:
        return "Non-positive"


def classify_number(x):
    if x < 0:
        return "Negative"
    elif x == 0:
        return "Zero"
    else:
        return "Positive"
    
def process_numbers(nums):
    evens = 0
    odds = 0
    for num in nums:
        if num % 2 == 0:
            print(f"{num} is even")
            evens += 1
        else:
            print(f"{num} is odd")
            odds += 1
    return evens, odds


def analyze_data(data):
    evens = 0
    odds = 0
    for item in data:
        if isinstance(item, int):
            if item % 2 == 0:
                evens += 1
            else:
                odds += 1
        else: 
            raise ValueError("Invalid data type")
    return evens, odds
