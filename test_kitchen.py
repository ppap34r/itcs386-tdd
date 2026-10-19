# Part A1: The first failing test
# from kitchen import Quantity
from kitchen import Quantity, grams, ounces

# def test_multiplication():
#     flour = Quantity(200)
#     flour.times(3)
#     assert flour.amount == 600

# Part A2: Triangulating to the real formula
# def test_multiplication_by_two():
#     flour = Quantity(200)
#     flour.times(2)
#     assert flour.amount == 400

# A3: A quantity that does not change under you
# def test_multiplication():
#     flour = Quantity(200)
#     assert flour.times(3).amount == 600

# def test_multiplication_returns_a_new_quantity():
#     flour = Quantity(200)
#     assert flour.times(3).amount == 600
#     assert flour.times(2).amount == 400

# A4: Equality
# def test_equality():
#     assert Quantity(200) == Quantity(200)
#     assert Quantity(200) != Quantity(300)

# def test_multiplication():
#     flour = Quantity(200)
#     assert flour.times(3) == Quantity(600)

# def test_multiplication_returns_a_new_quantity():
#     flour = Quantity(200)
#     assert flour.times(3) == Quantity(600)
#     assert flour.times(2) == Quantity(400)

# A5: A second unit
# def test_grams_are_not_ounces():
#     assert Quantity(1, "g") != Quantity(1, "oz")

# def test_equality():
#     assert Quantity(200, "g") == Quantity(200, "g")
#     assert Quantity(200, "g") != Quantity(300, "g")


# def test_multiplication():
#     flour = Quantity(200, "g")
#     assert flour.times(3) == Quantity(600, "g")


# def test_multiplication_returns_a_new_quantity():
#     flour = Quantity(200, "g")
#     assert flour.times(3) == Quantity(600, "g")
#     assert flour.times(2) == Quantity(400, "g")

# Refactor
def test_equality():
    assert grams(200) == grams(200)
    assert grams(200) != grams(300)


def test_multiplication():
    flour = grams(200)
    assert flour.times(3) == grams(600)


def test_multiplication_returns_a_new_quantity():
    flour = grams(200)
    assert flour.times(3) == grams(600)
    assert flour.times(2) == grams(400)


def test_grams_are_not_ounces():
    assert grams(1) != ounces(1)