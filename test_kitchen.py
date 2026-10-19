# Part A1: The first failing test
from kitchen import Quantity

def test_multiplication():
    flour = Quantity(200)
    flour.times(3)
    assert flour.amount == 600

# Part A2: Triangulating to the real formula
def test_multiplication_by_two():
    flour = Quantity(200)
    flour.times(2)
    assert flour.amount == 400
    