import pytest
from shipping import shipping_fee


# Rule 1: Weight must be more than 0 kg
@pytest.mark.parametrize("weight", [0, -1])
def test_invalid_weight_is_rejected(weight):
    with pytest.raises(ValueError):
        shipping_fee(weight)


# Rule 2: Up to 1 kg costs 40 baht
@pytest.mark.parametrize("weight, expected", [
    (0.5, 40),
    (1, 40),
])
def test_light_parcel_costs_40(weight, expected):
    assert shipping_fee(weight) == expected


# Rule 3: More than 1 kg and up to 5 kg costs 60 baht
@pytest.mark.parametrize("weight, expected", [
    (1.1, 60),
    (3, 60),
    (5, 60),
])
def test_medium_parcel_costs_60(weight, expected):
    assert shipping_fee(weight) == expected


# Rule 4: More than 5 kg costs 60 baht plus 10 baht per started kg
@pytest.mark.parametrize("weight, expected", [
    (5.2, 70),
    (6, 70),
    (7.1, 90),
])
def test_heavy_parcel_fee(weight, expected):
    assert shipping_fee(weight) == expected
