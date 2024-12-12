# test_ninth.py

from ninth import dev_to_bin

def test_dev_to_bin():
    # Test pro celé číslo
    assert dev_to_bin(167) == "10100111"
    
    # Test pro řetězec jako vstup
    assert dev_to_bin("167") == "10100111"
    
    # Test pro jiné číslo
    assert dev_to_bin(0) == "0"
    
    # Test pro další číslo
    assert dev_to_bin(255) == "11111111"
    
    # Test pro malé číslo
    assert dev_to_bin(5) == "101"
    
    # Test pro jiné malé číslo
    assert dev_to_bin(7) == "111"
