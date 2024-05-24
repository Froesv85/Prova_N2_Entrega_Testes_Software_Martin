import pytest
from stat_funcs import StatsN2

@pytest.fixture
def stats_instance():
    return StatsN2()

@pytest.mark.parametrize("lista, pesos, expected", [
    ([1, 2, 3], [0.8, 0.5, 0.7], 1.9499999999999997),
    ([10, 20, 30], [0.2, 0.3, 0.5], 23.0),
    ([0, 0, 0], [0.1, 0.1, 0.1], 0.0),
    ([2, 4, 8], [0.1, 0.2, 0.3], 5.666666666666666),
    ([1, 3, 5], [0.2, 0.3, 0.5], 3.4),
    ([1, 1, 1], [0.1, 0.1, 0.1], 1.0),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [0.1, 0.2, 0.3, 0.1, 0.2, 0.3, 0.1, 0.2, 0.3, 0.1], 5.5),
])
def test_media_ponderada(stats_instance, lista, pesos, expected):
    assert stats_instance.media_ponderada(lista, pesos) == expected
@pytest.mark.xfail
def test_xmedia_ponderad(stats_instance, pesos):
        assert stats_instance.media_ponderada(pesos) == 0.45
