import pytest
from stat_funcs import StatsN2


@pytest.fixture
def stats_instance():
    return StatsN2()


@pytest.mark.parametrize("lista, expected", [
    ([1, 2, 3, 4, 5], "Existe moda"),
    ([10, 20, 30, 20, 10], "Não existe moda"),
    ([1, 2, 3, 4, 4], "Existe moda"),
    ([10, 20, 30, 50, 10], "Não existe moda"),
    ([9, 9, 9, 4, 5], "Existe moda"),
    ([170, 290, 360, 250, 130], "Não existe moda"),
])

def test_amodal(stats_instance, lista, expected):
    assert stats_instance.amodal(lista) == expected


@pytest.mark.xfail
def test_xamodal(stats_instance, numeros_amodal):
    assert stats_instance.amodal(numeros_amodal) == "Existe moda"
