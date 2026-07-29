# Pytest in a nutshell Part 2/2

from pytest_real import add, calculate_profit, calculated_profit_advanced

def test_add():
    assert add(2,3) == 5

def test_profit():
    assert calculate_profit(50,80) == 30

# This will show an error 
def test_profit_advanced_wrong():
    assert calculated_profit_advanced(50,80) == 29

def test_profit_advanced():
    assert calculated_profit_advanced(50,80,1) == 29