import cfg_examples as examples

def test_check_number():
    assert examples.check_number(5) == "Positive"

if __name__ == "__main__":
    test_check_number()
    print("All tests passed!")