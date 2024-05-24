import pytest
from stat_funcs import StatsN2

@pytest.fixture
def stats_instance():
    return StatsN2()

@pytest.mark.parametrize("lista, expected", [
    ([1, 2, 3, 4, 5], 2.5),
    ([10, 20, 30, 20, 10], 50.0),
    ([0, 0, 0, 0, 0], 0.0),
    ([1, 1, 1, 1, 1], 0.0),
    ([1, 2, 3, 4, 5, 6], 3.5),
    ([5, 5, 5, 5, 5, 5], 0.0),
    ([1, 3, 5, 7, 9], 8.0),
])
def test_variancia(stats_instance, lista, expected):
    assert stats_instance.variancia(lista) == expected

@pytest.mark.xfail
def test_xvariancia(stats_instance, pesos):
    assert stats_instance.variancia(pesos) == 0.45
