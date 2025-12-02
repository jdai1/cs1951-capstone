import pytest


def assert_equal_hundredths(a, b):
    if round(a, 2) != round(b, 2):
        raise AssertionError(f"{a} != {b} (to hundredths)")

@pytest.mark.parametrize(
    "v, x, y, expected", 
    [
        (0.5, 10, 10, 10), 
        (0.6, 10, 10, 8.16), 
        (0.7, 10, 10, 6.55), 
        (0.8, 10, 10, 5.00), 
        (0.9, 10, 10, 3.33), 
    ]
)
def test_value_to_stable_state(w3, HAY_token, HAY_exchange, DEN_token, DEN_exchange, v, x, y, expected):
    x =  HAY_exchange.valueToStableState(int(v * 10**18), x * 10**18, y * 10**18)
    assert_equal_hundredths(x / 10**18, expected)
    


@pytest.mark.parametrize(
    "x, y, eth_reserve, expected", 
    [
        (10, 10, 4, 0.86), 
        (10, 10, 5, 0.80), 
        (10, 10, 10, 0.50), 
        (10, 10, 25, 0.14), 
    ]
)
def test_stable_state_to_value(w3, HAY_token, HAY_exchange, DEN_token, DEN_exchange, x, y, eth_reserve, expected):
    v = HAY_exchange.stableStateToValue(x * 10**18, y * 10**18, eth_reserve * 10**18)
    assert_equal_hundredths(v / 10**18, expected)