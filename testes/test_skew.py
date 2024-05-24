import pytest
from stat_funcs import StatsN2

@pytest.fixture
def stats_instance():
    return StatsN2()

@pytest.mark.parametrize("lista, expected", [
    ([1, 2, 3, 4, 5], "Distribuição positiva"),
    ([10, 20, 30, 20, 10], "Distribuição negativa"),
    ([0, 0, 0, 0, 0], "Distribuição positiva"),
    ([1, 1, 1, 1, 1], "Distribuição positiva"),
    ([1, 2, 3, 4, 5, 6], "Distribuição positiva"),
    ([5, 5, 5, 5, 5, 5], "Distribuição positiva"),
    ([1, 3, 5, 7, 9], "Distribuição positiva"),
    ([9, 7, 5, 3, 1], "Distribuição negativa"),
])
def test_skew(stats_instance, lista, expected):
    assert stats_instance.skew(lista) == expected

@pytest.mark.xfail
def test_xskew(stats_instance, lista_de_numeros):
    assert stats_instance.skew(lista_de_numeros) == "NDistribuição negativa"

