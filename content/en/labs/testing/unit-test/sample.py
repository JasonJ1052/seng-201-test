def palindrome_check(s):
    cleaned_str = ''.join(s.lower()) 
    return cleaned_str == cleaned_str[::-1]

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def reverse_string(s):
    return s[::-1]


if __name__ == "__main__":
    print(palindrome_check("kayak"))
    print(palindrome_check("Kayak"))
    print(palindrome_check("moose"))

    print(is_prime(1))
    print(is_prime(7))
    print(is_prime(8))

