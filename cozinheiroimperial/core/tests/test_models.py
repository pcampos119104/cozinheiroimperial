import pytest
from model_bakery import baker


pytestmark = pytest.mark.django_db

'''
def test_segmento_str(segmento: Segmento) -> None:
    assert f"{segmento.nome}" == str(segmento)


def test_segmento_obj(segmento: Segmento) -> None:
    assert isinstance(segmento, Segmento)


def test_categoria_str(categoria: Categoria) -> None:
    assert f"{categoria.nome}" == str(categoria)


def test_categoria_obj(categoria: Categoria) -> None:
    assert isinstance(categoria, Categoria)


def test_marca_str(marca: Marca) -> None:
    assert f"{marca.nome}" == str(marca)


def test_marca_obj(marca: Marca) -> None:
    assert isinstance(marca, Marca)


def test_produto_str(produto: Produto) -> None:
    assert f"{produto.gtin} {produto.descricao}" == str(produto)


def test_produto_obj(produto: Produto) -> None:
    assert isinstance(produto, Produto)


def test_produto_fk(produto: Produto) -> None:
    assert isinstance(produto.marca, Marca)
    assert isinstance(produto.segmento, Segmento)
'''
