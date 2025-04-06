"""Unit Tests for Exercise 03 - Dictionary Functions"""

__author__ = "730567850"

import pytest
from exercises.ex03.dictionary import invert, favorite_color, count, bin_len


def test_invert_use():
    """Test normal dictionary inversion."""
    assert invert({"a": "z", "b": "y", "c": "x"}) == {"z": "a", "y": "b", "x": "c"}


def test_invert_use_one_pair():
    """Test normal dictionary inversion with one pair."""
    assert invert({"k": "g"}) == {"g": "k"}


def test_invert_edge():
    """Test if duplicate values leads to KeyError."""
    with pytest.raises(KeyError):
        my_dictionary = {"kris": "jordan", "michael": "jordan"}
        invert(my_dictionary)


def test_count_use():
    """Test normal count function."""
    assert count(["cheese", "milk", "cheese"]) == {"cheese": 2, "milk": 1}


def test_count_all_same():
    """Test normal count function with all same items."""
    assert count(["cheese", "cheese", "cheese"]) == {"cheese": 3}


def test_count_edge_empty():
    """Test count function if the list is empty."""
    assert count([]) == {}


def test_favorite_color_use():
    """Test normal favorite color function."""
    assert (
        favorite_color(
            {"Billy": "red", "Annie": "blue", "Suzy": "purple", "Tommy": "blue"}
        )
        == "blue"
    )


def test_favorite_color_use_tie():
    """Test that favorite color is the first listed if tie."""
    assert (
        favorite_color(
            {"Billy": "red", "Annie": "blue", "Suzy": "red", "Tommy": "blue"}
        )
        == "red"
    )


def test_favorite_color_edge_one():
    """Test favorite color when only one person."""


def test_favorite_color_tie():
    """Test favorite color when there's a tie."""
    assert favorite_color({"Alice": "blue"}) == "blue"


def test_bin_len_use():
    """Test normal bin function."""
    assert bin_len(["ham", "and", "cheese"]) == {3: {"ham", "and"}, 6: {"cheese"}}


def test_bin_len_use_all_dif():
    """Test normal bin when all words are different lengths."""
    assert bin_len(["i", "need", "sleep"]) == {1: {"i"}, 4: {"need"}, 5: {"sleep"}}


def test_bin_len_edge():
    """Test bin_len when empty list."""
    assert bin_len([]) == {}
