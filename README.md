This is a capstone project for CS1951L, Blockchains.

The uniswap code is forked from [here](https://github.com/PhABC/uniswap-solidity).

The handout can be found [here](https://drive.google.com/file/d/10VWOLpUqv56RJATp_pIFcz-jdYuC9g1Y/view).

The files relevant to the project are:
- `UniswapExchange.sol` L619 and onwards
- `test_div_loss.py`
- `test_lin_slip.py`
- `test_ang_slip.py`
- `test_load.py`

There were some complications with getting things up and running since the base repo is quite outdated! Once you install all the dependencies (e.g. via `yarn install`), run tests by running `yarn build && pytest -v path_to_your_test`.
