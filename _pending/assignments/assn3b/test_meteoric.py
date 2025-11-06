"""Unit test for meteoric.py"""
import meteoric


def test_load_data():
    """Test case for load_data()"""
    result = meteoric.load_data()
    assert result[0] == ['Aachen', '1', '1880', '50.775', '6.08333']
    assert result[-1] == ['Zulu Queen', '30414', '1976', '33.98333', '-115.68333']
