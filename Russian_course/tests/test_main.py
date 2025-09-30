import pytest
from main import A, Calculator
from contextlib import nullcontext as does_not_raise

def test_main():
    assert A.x == 1

class TestCalculator:
    @pytest.mark.parametrize(
        "x,y,res,expectation",
        [
            (8, 4, 2, does_not_raise),
            (6, 2, 3, does_not_raise),
            (6, "2", 3, pytest.raises(TypeError))
        ]
    )
    def test_divide(self, x, y, res, expectation):
        with expectation:
            assert Calculator.divide(x, y) == res 

    @pytest.mark.parametrize(
        "x,y,res",
        [
            (2, 5, 7),
            (8, "3", 11)
        ]
    )
    def test_add(self, x, y, res):
        calc = Calculator()
        assert calc.add(x, y) == res


