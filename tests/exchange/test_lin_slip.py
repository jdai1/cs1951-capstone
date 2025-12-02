import pytest

def assert_equal_hundredths(a, b):
    if round(a, 2) != round(b, 2):
        raise AssertionError(f"{a} != {b} (to hundredths)")


@pytest.mark.parametrize(
    "x, y, eth_sold, expected", 
    [
        (10, 10, 1, 0.0498), 
        (10, 10, 2, 0.197), 
        (10, 10, 5, 1.154), 
    ]
)
def test_get_eth_to_token_linear_slippage(w3, HAY_token, HAY_exchange, DEN_token, DEN_exchange, x, y, eth_sold, expected):
    x =  HAY_exchange.getEthToTokenLinearSlippage(x * 10**18, y * 10**18, eth_sold * 10**18)
    print(f"{x:,}")
    assert_equal_hundredths(x / 10**18, expected)


@pytest.mark.parametrize(
    "x, y, token_sold, expected", 
    [
        (10, 10, 1, 0.0411), 
        (10, 10, 2, 0.137), 
        (10, 10, 5, 0.513), 
    ]
)
def test_get_token_to_eth_linear_slippage(w3, HAY_token, HAY_exchange, DEN_token, DEN_exchange, x, y, token_sold, expected):
    x =  HAY_exchange.getTokenToEthLinearSlippage(x * 10**18, y * 10**18, token_sold * 10**18)
    print(f"{x:,}")
    assert_equal_hundredths(x / 10**18, expected)