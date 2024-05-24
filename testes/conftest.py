import pytest
from stat_funcs import StatsN2

@pytest.fixture
def stats_instance():
    return StatsN2()

@pytest.fixture
def lista_de_numeros():
    return [1, 2, 3, 4, 5]
@pytest.fixture
def numeros_unimodal ():
    return [5, 7, 9, 10, 12, 13, 14, 15, 16, 17, 18]
@pytest.fixture
def numeros_multimodal ():
    return [1, 2, 2, 3, 3, 4, 4, 5 , 6, 7, 8, 9, 10]
@pytest.fixture
def numeros_amodal ():
    return [1, 2, 3, 4, 5 ]
@pytest.fixture
def pesos ():
    return [0.1, 0.2, 0.3, 0.2, 0.2]

@pytest.mark.xfail
def test_xmedia(stats_instance, lista_de_numeros):
    expected_media = 3.0
    assert stats_instance.media(lista_de_numeros) == expected_media


def test_xmedia_ponderada(stats_instance, lista, pesos, expected):
    assert stats_instance.media_ponderada(lista, pesos) == expected
@pytest.mark.xfail
def test_xunimodal(stats_instance, numeros_unimodal):
    assert stats_instance.unimodal(numeros_unimodal) == "Não é unimodal"
@pytest.mark.xfail
def test_xmultimodal(stats_instance, numeros_multimodal):
    assert stats_instance.multimodal(numeros_multimodal) == "Não é multimodal"
@pytest.mark.xfail
def test_xamodal(stats_instance, numeros_amodal):
    assert stats_instance.amodal(numeros_amodal) == "Existe moda"
@pytest.mark.xfail
def test_xvariancia(stats_instance, pesos):
    expected_variancia = 2.5
    assert stats_instance.variancia(pesos) == expected_variancia
@pytest.mark.xfail
def test_xdpadrao(stats_instance, lista_de_numeros):
    expected_dpadrao = 1.5811388300841898
    assert stats_instance.dpadrao(stats_instance.variancia(lista_de_numeros)) == expected_dpadrao
@pytest.mark.xfail
def test_xkew(stats_instance, lista_de_numeros):
    expected_skew = "Distribuição positiva"
    assert stats_instance.skew(lista_de_numeros) == expected_skew
