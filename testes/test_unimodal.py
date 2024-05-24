# test_unimodal.py
import pytest
from stat_funcs import StatsN2

@pytest.fixture
def stats_instance():
    return StatsN2()

@pytest.mark.parametrize("lista, expected", [
    ([1, 2, 3, 4, 5], "Não é unimodal"),
    ([10, 20, 30, 20, 10], 20),
    ([1, 2, 3, 4, 5, 6], "Não é unimodal"),
    ([10, 20, 30, 40, 50, 60], [20, 30]),
    ([1, 2, 3, 4, 5, 5, 5], 5),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [5, 6]),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "Não é unimodal"),
])
def test_unimodal(stats_instance, lista, expected):
    assert stats_instance.unimodal(lista) == expected

@pytest.mark.xfail
def test_xunimodal(stats_instance, numeros_unimodal):
    assert stats_instance.unimodal(numeros_unimodal) == "Não é unimodal"

