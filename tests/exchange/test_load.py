import pytest

def assert_equal_hundredths(a, b):
    if round(a, 2) != round(b, 2):
        raise AssertionError(f"{a} != {b} (to hundredths)")


@pytest.mark.parametrize(
    "x, y, eth_sold", 
    [
        (10, 10, 1),
        (10, 10, 2),
        (10, 10, 3),
        (10, 10, 5),
        (10, 20, 5),
        (20, 10, 3),
        (100, 100, 10),
    ]
)
def test_get_eth_to_token_load(w3, HAY_token, HAY_exchange, DEN_token, DEN_exchange, x, y, eth_sold):
    """Test that Load = DivergenceLoss * LinearSlippage / 1e18"""
    x_scaled = x * 10**18
    y_scaled = y * 10**18
    eth_sold_scaled = eth_sold * 10**18
    
    # Get the load directly
    load = HAY_exchange.getEthToTokenLoad(x_scaled, y_scaled, eth_sold_scaled)
    
    # Calculate load from components
    div_loss = HAY_exchange.getEthToTokenDivergenceLoss(x_scaled, y_scaled, eth_sold_scaled)
    lin_slip = HAY_exchange.getEthToTokenLinearSlippage(x_scaled, y_scaled, eth_sold_scaled)
    expected_load = div_loss * lin_slip // 10**18
    
    # Convert to human-readable for comparison
    load_human = load / 10**18
    expected_load_human = expected_load / 10**18
    
    print(f"x={x}, y={y}, eth_sold={eth_sold}")
    print(f"  Load: {load_human:.6f}")
    print(f"  Expected (DivLoss * LinSlip): {expected_load_human:.6f}")
    print(f"  DivLoss: {div_loss / 10**18:.6f}, LinSlip: {lin_slip / 10**18:.6f}")
    
    assert_equal_hundredths(load_human, expected_load_human)


@pytest.mark.parametrize(
    "x, y, token_sold", 
    [
        (10, 10, 1),
        (10, 10, 2),
        (10, 10, 3),
        (10, 10, 5),
        (20, 10, 5),
        (10, 20, 3),
        (100, 100, 10),
    ]
)
def test_get_token_to_eth_load(w3, HAY_token, HAY_exchange, DEN_token, DEN_exchange, x, y, token_sold):
    """Test that Load = DivergenceLoss * LinearSlippage / 1e18"""
    x_scaled = x * 10**18
    y_scaled = y * 10**18
    token_sold_scaled = token_sold * 10**18
    
    # Get the load directly
    load = HAY_exchange.getTokenToEthLoad(x_scaled, y_scaled, token_sold_scaled)
    
    # Calculate load from components
    div_loss = HAY_exchange.getTokenToEthDivergenceLoss(x_scaled, y_scaled, token_sold_scaled)
    lin_slip = HAY_exchange.getTokenToEthLinearSlippage(x_scaled, y_scaled, token_sold_scaled)
    expected_load = div_loss * lin_slip // 10**18
    
    # Convert to human-readable for comparison
    load_human = load / 10**18
    expected_load_human = expected_load / 10**18
    
    print(f"x={x}, y={y}, token_sold={token_sold}")
    print(f"  Load: {load_human:.6f}")
    print(f"  Expected (DivLoss * LinSlip): {expected_load_human:.6f}")
    print(f"  DivLoss: {div_loss / 10**18:.6f}, LinSlip: {lin_slip / 10**18:.6f}")
    
    assert_equal_hundredths(load_human, expected_load_human)

