import sample  # We import the filename without the .py

def test_palindrome():
    assert sample.palindrome_check("kayak")  # the function should return True, giving "assert True"
    assert sample.palindrome_check("Kayak")
    assert sample.palindrome_check("moose") is False  # the function should return False, giving "assert False is False", which is True

def test_is_prime():
    assert sample.is_prime(1) is False
    assert sample.is_prime(2)
    assert sample.is_prime(8) is False

def test_reverse():
    assert sample.reverse_string("press") == "sserp"  # checking result for equality with expected
    assert sample.reverse_string("alice") == "ecila"
    assert sample.reverse_string("") == ""

# run the test cases when executing the file
if __name__ == "__main__": 
    test_palindrome()
    test_is_prime()
    test_reverse()