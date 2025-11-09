import pytest

from sorting__package.bubble_sort import bubble_sort


@pytest.mark.parametrize(
    ["input_data", "expected_output"],
    [
        ([10, 3, 2, -67, 52], [-67, 2, 3, 10, 52]),
        ([1, 2, 3], [1, 2, 3]),
        ([3, 2, 1], [1, 2, 3]),
        ([100, 33, 55, 66], [33, 55, 66, 100]),
    ],
)
def test_bubble_sort(input_data, expected_output):
    result = bubble_sort(input_data)
    assert result == expected_output


def test_bubble_sort_edge_cases():
    assert bubble_sort([1]) == [1]
    assert bubble_sort([]) == []
    assert bubble_sort([5, 5, 5]) == [5, 5, 5]
