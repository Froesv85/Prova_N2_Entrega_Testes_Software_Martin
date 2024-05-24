# test_mediana.py
import pytest
from stat_funcs import StatsN2

@pytest.fixture
def stats_instance():
    return StatsN2()

@pytest.mark.parametrize("lista, expected", [
    ([1, 2, 3, 4, 5], 3),
    ([10, 20, 30, 40, 50], 30),
    ([0, 0, 0, 0, 0], 0),
    ([2, 4, 6, 8, 10], 6),
    ([1, 3, 5, 7, 9], 5),
    ([1, 1, 1, 1, 1], 1),
    ([6, 7, 9, 12, 13, 4, 2, 15, 19, 10], 10),
])
def test_mediana(stats_instance, lista, expected):
    assert stats_instance.mediana(lista) == expected
