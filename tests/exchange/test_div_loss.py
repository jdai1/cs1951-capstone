import pytest

def assert_equal_hundredths(a, b):
    if round(a, 2) != round(b, 2):
        raise AssertionError(f"{a} != {b} (to hundredths)")
    


@pytest.mark.parametrize(
    "x, y, eth_sold, expected", 
    [
        (10, 10, 1, 0.0452), 
        (10, 10, 2, 0.164), 
        (10, 10, 3, 0.334), 
        (10, 10, 5, 0.769), 
        (10, 20, 5, 1.176)
        
    ]
)
def test_get_eth_to_token_divergence_loss(w3, HAY_token, HAY_exchange, DEN_token, DEN_exchange, x, y, eth_sold, expected):
    x =  HAY_exchange.getEthToTokenDivergenceLoss(x * 10**18, y * 10**18, eth_sold * 10**18)
    assert_equal_hundredths(x / 10**18, expected)


@pytest.mark.parametrize(
    "x, y, token_sold, expected", 
    [
        (10, 10, 1, 0.0452), 
        (10, 10, 2, 0.164), 
        (10, 10, 3, 0.334), 
        (10, 10, 5, 0.769), 
        (20, 10, 5, 1.176)
    ]
)
def test_get_token_to_eth_divergence_loss(w3, HAY_token, HAY_exchange, DEN_token, DEN_exchange, x, y, token_sold, expected):
    x =  HAY_exchange.getTokenToEthDivergenceLoss(x * 10**18, y * 10**18, token_sold * 10**18)
    assert_equal_hundredths(x / 10**18, expected)