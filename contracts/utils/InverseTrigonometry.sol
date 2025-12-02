pragma solidity ^0.5.0;

library InverseTrigonometry {
   function sqrt(uint256 y) internal pure returns (uint256 z) {
      if (y > 3) {
          z = y;
          uint x = y / 2 + 1;
          while (x < z) {
              z = x;
              x = (y / x + x) / 2;
          }
      } else if (y != 0) {
          z = 1;
      }
  }


  function g(int256 _x) internal pure returns (int256) {
    int256 ONE = 1000000000000000000;
    // 1.5707288
    int256 a0 = 1570728800000000000;
    // −0.2121144
    int256 a1 = -212114400000000000;
    // 0.0742610
    int256 a2 = 74261000000000000;
    // −0.0187293
    int256 a3 = -18729300000000000;

    int256 PI = 3141592653589793238;
    int256 HALF_PI = PI / 2; 

    // Multiply by ONE before sqrt to maintain 18 decimal precision
    int256 root = int256(sqrt(uint256(ONE - _x) * uint256(ONE)));

    // Properly scale polynomial: a0 + x*(a1 + x*(a2 + x*a3))
    int256 inner = a2 + (_x * a3) / ONE;
    inner = a1 + (_x * inner) / ONE;
    int256 poly = a0 + (_x * inner) / ONE;

    return HALF_PI - (root * poly) / ONE;
  }

  function f(int256 _x) internal pure returns (int256) {
    int256 ONE = 1000000000000000000;
    int256 xSq = (_x * _x) / ONE;

    // 1/6
    // https://www.wolframalpha.com/input?i=1%2F6
    // 0.1666666666666666666666666
    int256 frac1Div6 = 166666666666666666;

    // 3/40
    // https://www.wolframalpha.com/input?i=3%2F40
    // 0.075
    int256 frac3Div40 = 75000000000000000;

    // 15/336
    // https://www.wolframalpha.com/input?i=15%2F336
    // 0.044642857142857142857142857142
    int256 frac15Div336 = 44642857142857142;

    // Properly scale: x * (1 + x^2*(1/6 + x^2*(3/40 + x^2*15/336)))
    int256 inner = frac3Div40 + (xSq * frac15Div336) / ONE;
    inner = frac1Div6 + (xSq * inner) / ONE;
    int256 poly = ONE + (xSq * inner) / ONE;

    return (_x * poly) / ONE;
  }

  /**
     * @notice Arcsine function
     *
     * @param _x A integer with 18 fixed decimal points, where the whole part is bounded inside of [-1,1]
     *
     * @return The arcsine, with 18 fixed decimal points
     */
  function arcsin(int256 _x) internal pure returns (int256) {
    int256 DOMAIN_MAX = 1000000000000000000;
    int256 DOMAIN_MIN = -DOMAIN_MAX;
    require(_x >= DOMAIN_MIN && _x <= DOMAIN_MAX);

    // arcsin is an odd function, so arcsin(-x) = -arcsin(x), so we can remove
    // the negative here for easier math
    bool isNegative = _x < 0;
    _x = isNegative ? -_x : _x;

    // 0.4788
    int256 CHOICE_LINE = 478800000000000000;

    int256 result = _x < CHOICE_LINE ? f(_x) : g(_x);

    return isNegative ? -result : result;
  }

  /**
   * @notice Arctangent function
   * @dev Uses the identity: atan(x) = arcsin(x / sqrt(1 + x^2))
   * @param _x Input value with 18 decimal precision
   * @return Arctangent result with 18 decimal precision
   */
  function atan(int256 _x) internal pure returns (int256) {
    int256 ONE = 1000000000000000000;

    // Calculate x^2 with proper fixed-point scaling
    int256 xsq = (_x * _x) / ONE;
    
    // Calculate 1 + x^2 (x^2 is always non-negative, so 1 + x^2 >= 1)
    int256 onePlusXsq = ONE + xsq;
    require(onePlusXsq > 0, "InverseTrigonometry#atan: OVERFLOW");
    
    // Calculate sqrt(1 + x^2) with proper fixed-point scaling
    // Multiply by ONE before sqrt to maintain 18 decimal precision
    int256 denom = int256(sqrt(uint256(onePlusXsq) * uint256(ONE)));

    // Calculate x / sqrt(1 + x^2) with proper fixed-point division
    int256 ratio = (_x * ONE) / denom;

    // Use arcsin: atan(x) = arcsin(x / sqrt(1 + x^2))
    return arcsin(ratio);
  }
}

