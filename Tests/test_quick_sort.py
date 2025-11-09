import pytest

from sorting__package.quick_sort import quick_sort


@pytest.mark.parametrize(
    ["input_data", "expected_output"],
    [
        ([4, 3, 2, 0, -1, 4, 3], [-1, 0, 2, 3, 3, 4, 4]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
    ],
)
def test_quick_sort(input_data, expected_output):
    result = quick_sort(input_data)
    assert result == expected_output


def test_quick_sort_edge_cases():
    assert quick_sort([1]) == [1]
    assert quick_sort([]) == []
