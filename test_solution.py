import pytest

from example_test_cases import EXAMPLE_TEST_CASES
from my_solution import largestRectangleArea
from meta_ai_solution import largestRectangleArea as lra


@pytest.mark.parametrize("case", EXAMPLE_TEST_CASES, ids=lambda case: case["name"])
def test_largest_rectangle_area(case):
    heights = case["heights"]
    expected = case["expected"]

    result = largestRectangleArea(heights)
    assert result == expected


@pytest.mark.parametrize("case", EXAMPLE_TEST_CASES, ids=lambda case: case["name"])
def test_lra(case):
    heights = case["heights"]
    expected = case["expected"]

    result = lra(heights)
    assert result == expected


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__]))
