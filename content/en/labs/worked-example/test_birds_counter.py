# this is the unit test of the program file birds_counter.py
import birds_counter
import pytest

def test_count_birds():
    # Testing entails checking the ACTUAL result against the EXPECTED result
    # for a given input

    # When you make tests, YOU THE TESTER define the EXPECTED result
    expected = {
        "White-eared Hummingbird" : 1,
        "Red-shouldered Blackbird" : 1,
        "Townsend's Solitaire": 2,
        "Yellow-fronted Canary" : 1
    }
    # birds_counter.count_birds('birds_test.txt') gives us the ACTUAL result
    assert birds_counter.count_birds('birds_test.txt') == expected
    assert birds_counter.count_birds('birds_test.txt   ') == expected
    assert birds_counter.count_birds('birds_empty.txt') == {}

def test_count_birds_bad_filenames():
    with pytest.raises(ValueError) as verr:
        birds_counter.count_birds('')
    assert str(verr.value) == "You need to enter a valid filename ending in .txt"

    with pytest.raises(ValueError) as verr:
        birds_counter.count_birds('a.txt.exe')
    assert str(verr.value) == "You need to enter a valid filename ending in .txt"

def test_count_birds_bad_files():    
    with pytest.raises(FileNotFoundError) as ferr:
        birds_counter.count_birds('noexisto.txt')
    
    with pytest.raises(UnicodeDecodeError) as uerr:
        birds_counter.count_birds('bad.txt')
    