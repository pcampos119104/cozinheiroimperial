import pytest
from django.test import RequestFactory
from django.urls import reverse
from model_bakery import baker

from cozinheiroimperial.django_assertions import assert_contains

pytestmark = pytest.mark.django_db


class TestHomeView:
    def test_home_view(self, client):
        resp = client.get(reverse("home"))
        assert resp.status_code == 200


class TestRecipesView:
    def test_home_view(self, client):
        resp = client.get(reverse("core:recipes"))
        assert resp.status_code == 200


'''
    def test_marca_create_view(self, client):
        resp = client.get(reverse("produtos:marca-create"))
        assert_contains(resp, "id_nome")

    def test_marca_delete_view(self, client, marca: Marca):
        marca = baker.make(Marca, _fill_optional=True, deleted_at=None)
        resp = client.delete(reverse("produtos:marca-delete", args=(marca.id,)))
        assert_contains(resp, '"ok": true')

    def test_marca_update_view(self, client, marca: Marca):
        resp = client.get(reverse("produtos:marca-update", args=(marca.id,)))
        assert_contains(resp, marca.nome)


class TestSegmentoView:
    def test_segmento_list_view(self, client):
        segmentos = baker.make(Segmento, 5, _fill_optional=True, deleted_at=None)
        resp = client.get(reverse("produtos:segmento-list"))
        assert_contains(resp, segmentos[0].nome)
        assert_contains(resp, segmentos[-1].nome)

    def test_segmento_create_view(self, client):
        resp = client.get(reverse("produtos:segmento-create"))
        assert_contains(resp, "id_nome")

    def test_segmento_delete_view(self, client):
        segmento = baker.make(Segmento, _fill_optional=True, deleted_at=None)
        resp = client.delete(reverse("produtos:segmento-delete", args=(segmento.id,)))
        assert_contains(resp, '"ok": true')

    def test_segmento_update_view(self, client, segmento: Segmento):
        resp = client.get(reverse("produtos:segmento-update", args=(segmento.id,)))
        assert_contains(resp, segmento.nome)


class TestCategoriaView:
    def test_categoria_list_view(self, client):
        categorias = baker.make(Categoria, 5, _fill_optional=True, deleted_at=None)
        resp = client.get(reverse("produtos:categoria-list"))
        assert_contains(resp, categorias[0].nome)
        assert_contains(resp, categorias[-1].nome)

    def test_categoria_create_view(self, client):
        resp = client.get(reverse("produtos:categoria-create"))
        assert_contains(resp, "id_nome")

    def test_categoria_delete_view(self, client):
        categoria = baker.make(Categoria, _fill_optional=True, deleted_at=None)
        resp = client.delete(reverse("produtos:categoria-delete", args=(categoria.id,)))
        assert_contains(resp, '"ok": true')

    def test_categoria_update_view(self, client, categoria: Categoria):
        resp = client.get(reverse("produtos:categoria-update", args=(categoria.id,)))
        assert_contains(resp, categoria.nome)


class TestProdutoView:
    def test_produto_list_view(self, client):
        produtos = baker.make(Produto, 5, _fill_optional=True, deleted_at=None)
        resp = client.get(reverse("produtos:produto-list"))
        assert_contains(resp, produtos[0].descricao)
        assert_contains(resp, produtos[0].get_absolute_url())
        assert_contains(resp, produtos[-1].gtin)
        assert_contains(resp, produtos[-1].get_absolute_url())

    def test_produto_create_view(self, client):
        resp = client.get(reverse("produtos:produto-create"))
        assert_contains(resp, "marca")
        assert_contains(resp, "segmento")

    def test_produto_delete_view(self, client):
        produto = baker.make(Produto, _fill_optional=True, deleted_at=None)
        resp = client.delete(reverse("produtos:produto-delete", args=(produto.id,)))
        assert_contains(resp, '"ok": true')

    def test_produto_update_view(self, client, produto: Produto):
        resp = client.get(reverse("produtos:produto-update", args=(produto.id,)))
        assert_contains(resp, produto.descricao)
'''
