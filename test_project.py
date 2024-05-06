import project
import pytest

def test_add_numbers():
    assert project.add_numbers(1, 2) == 3
    assert project.add_numbers(1, 1) == 2