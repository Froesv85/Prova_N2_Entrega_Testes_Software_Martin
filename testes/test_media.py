import pytest
from stat_funcs import StatsN2


@pytest.fixture
def stats_instance():
    return StatsN2()


@pytest.mark.parametrize("lista, expected", [
    ([1, 2, 3, 4, 5], 3.0),
    ([10, 20, 30, 40, 50], 30.0),
    ([0, 0, 0, 0, 0], 0.0),
    ([2, 4, 6, 8, 10], 6.0),
    ([1, 3, 5, 7, 9], 4.0),
    ([1, 1, 1, 1, 1], 2.0),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5.5),
])
def test_media(stats_instance, lista, expected):
    assert stats_instance.media(lista) == expected


@pytest.mark.xfail
def test_xmedia(stats_instance, pesos):
    assert stats_instance.media(pesos) == 0.45
