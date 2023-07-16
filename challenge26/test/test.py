import pytest

from challenge26.Insertion_Sort import InsertionSort

def test_InsertionSort():
    # Test case 1: Input array is already sorted
    input_array = [1, 2, 3, 4, 5]
    sorted_array = InsertionSort(input_array)
    assert sorted_array == [1, 2, 3, 4, 5]

    # Test case 2: Input array is empty
    input_array = []
    sorted_array = InsertionSort(input_array)
    assert sorted_array == []

    # Test case 3: Input array is unsorted
    input_array = [5, 2, 4, 6, 1, 3]
    sorted_array = InsertionSort(input_array)
    assert sorted_array == [1, 2, 3, 4, 5, 6]

    # Test case 4: Input array with duplicate values
    input_array = [3, 2, 4, 1, 2, 3]
    sorted_array = InsertionSort(input_array)
    assert sorted_array == [1, 2, 2, 3, 3, 4]

    # Test case 5: Input array with negative values
    input_array = [-3, -2, -4, -1, -2, -3]
    sorted_array = InsertionSort(input_array)
    assert sorted_array == [-4, -3, -3, -2, -2, -1]