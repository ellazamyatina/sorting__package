import pytest

from sorting__package.merge_sort import merge_sort


@pytest.mark.parametrize(
    ["input_data", "expected_output"],
    [
        ([4, 3, 2, 0, -1, 4, 3], [-1, 0, 2, 3, 3, 4, 4]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
    ],
)
def test_merge_sort(input_data, expected_output):
    result = merge_sort(input_data)
    assert result == expected_output


def test_merge_sort_edge_cases():
    assert merge_sort([1]) == [1]
    assert merge_sort([]) == []
