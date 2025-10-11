import pytest
from streak import longest_positive_streak

def test_empty_list():
    """Test that an empty list returns a streak of 0."""
    assert longest_positive_streak([]) == 0

def test_single_streak():
    """Test a simple case with a single streak."""
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_multiple_streaks():
    """Test that the longest streak is returned when there are multiple."""
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_with_zeros():
    """Test that zeros break the streak."""
    assert longest_positive_streak([1, 2, 0, 3, 4, 5]) == 3

def test_with_negatives():
    """Test that negative numbers break the streak."""
    assert longest_positive_streak([1, -2, 3, 4, -5, 6]) == 2

def test_all_non_positive():
    """Test a list with no positive numbers."""
    assert longest_positive_streak([-1, -5, 0]) == 0

def test_all_same_positive():
    """Test a streak of identical positive numbers."""
    assert longest_positive_streak([1, 1, 1]) == 3

def test_streak_at_end():
    """Test when the longest streak is at the end of the list."""
    assert longest_positive_streak([-1, 0, 1, 2, 3, 4]) == 4

def test_streak_at_beginning():
    """Test when the longest streak is at the beginning of the list."""
    assert longest_positive_streak([1, 2, 3, 4, 0, -5]) == 4