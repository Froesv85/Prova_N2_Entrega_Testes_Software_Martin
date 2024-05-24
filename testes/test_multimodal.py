import pytest
from stat_funcs import StatsN2

@pytest.fixture
def stats_instance():
    return StatsN2()

@pytest.mark.parametrize("lista, expected", [
    ([1, 2, 3, 4, 5], "Não é multimodal"),
    ([10, 20, 30, 20, 10], [10,20]),
    ([1, 2, 3, 4, 5, 6], "Não é multimodal"),
    ([10, 20, 30, 40, 30, 20], [20, 30]),
    ([1, 2, 3, 4, 5, 5, 5], 5),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [5, 6]),
])
def test_multimodal(stats_instance, lista, expected):
    assert stats_instance.multimodal(lista) == expected

@pytest.mark.xfail
def test_xmultimodal(stats_instance, numeros_multimodal):
    assert stats_instance.mulimodal(numeros_multimodal) == "Não é multimodal"