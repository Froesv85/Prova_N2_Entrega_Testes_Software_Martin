
import pytest
from stat_funcs import StatsN2

@pytest.fixture
def stats_instance():
    return StatsN2()

@pytest.mark.parametrize("variancia, expected", [
    (25.0, 5.0),
    (50.0, 7.0710678118654755),
    (0.0, 0.0),
    (100.0, 10.0),
    (12.5, 3.5355339059327378),
    (10.0, 3.0),
    (30.0, 6.0),
])
def test_dpadrao(stats_instance, variancia, expected):
    assert stats_instance.dpadrao(variancia) == expected

@pytest.mark.xfail
def test_xdpadrao(stats_instance, lista_numeros):
    assert stats_instance.dpadrao(lista_numeros) == 3.12
