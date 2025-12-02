import pytest
import math


def assert_close(a, b, tolerance=0.01):
    """Assert two values are within tolerance of each other"""
    diff = abs(a - b)
    if diff > tolerance:
        raise AssertionError(f"{a} != {b} (difference: {diff}, tolerance: {tolerance})")


@pytest.mark.parametrize(
    "x, expected",
    [
        (0.0, 0.0),           # atan(0) = 0
        (1.0, math.pi / 4),   # atan(1) = π/4
        (-1.0, -math.pi / 4), # atan(-1) = -π/4
        (0.5, 0.4636),         # approximate
        (-0.5, -0.4636),       # approximate
    ]
)
def test_atan(w3, HAY_exchange, x, expected):
    """Basic sanity check tests for arctangent function"""
    x_scaled = int(x * 10**18)
    result_scaled = HAY_exchange.arctan(x_scaled)
    result = result_scaled / 10**18
    assert_close(result, expected, tolerance=0.01)


@pytest.mark.parametrize(
    "x, expected",
    [
        # Tests for f() path (|x| < 0.4788) - uses Taylor series
        (0.0, 0.0),                    # arcsin(0) = 0
        (0.1, math.asin(0.1)),         # arcsin(0.1) ≈ 0.1002
        (0.3, math.asin(0.3)),         # arcsin(0.3) ≈ 0.3047
        (-0.25, math.asin(-0.25)),     # arcsin(-0.25) ≈ -0.2527
        (0.4, math.asin(0.4)),         # arcsin(0.4) ≈ 0.4115
        (-0.4, math.asin(-0.4)),       # arcsin(-0.4) ≈ -0.4115
        
        # Tests for g() path (|x| >= 0.4788) - uses approximation
        (0.5, math.pi / 6),            # arcsin(0.5) = π/6
        (-0.5, -math.pi / 6),          # arcsin(-0.5) = -π/6
        (0.7, math.asin(0.7)),         # arcsin(0.7) ≈ 0.7754
        (1.0, math.pi / 2),            # arcsin(1) = π/2
        (-1.0, -math.pi / 2),          # arcsin(-1) = -π/2
    ]
)
def test_arcsin(w3, HAY_exchange, x, expected):
    """Basic sanity check tests for arcsine function"""
    x_scaled = int(x * 10**18)
    result_scaled = HAY_exchange.arcsin(x_scaled)
    result = result_scaled / 10**18
    assert_close(result, expected, tolerance=0.01)
