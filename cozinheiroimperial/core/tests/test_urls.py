import pytest
from django.urls import resolve, reverse

pytestmark = pytest.mark.django_db

'''
class TestRecipeUrls:
    def test_detail(self, segmento: Segmento) -> None:
        assert (
            reverse("produtos:segmento-detail", args=(segmento.id,))
            == f"/produtos/segmentos/{segmento.id}/"
        )
        assert (
            resolve(f"/produtos/segmentos/{segmento.id}/").view_name
            == "produtos:segmento-detail"
        )

    def test_update(self, segmento: Segmento) -> None:
        assert (
            reverse("produtos:segmento-update", args=(segmento.id,))
            == f"/produtos/segmentos/{segmento.id}/update/"
        )
        assert (
            resolve(f"/produtos/segmentos/{segmento.id}/update/").view_name
            == "produtos:segmento-update"
        )

    def test_list(self) -> None:
        assert reverse("produtos:segmento-list") == "/produtos/segmentos/"
        assert resolve("/produtos/segmentos/").view_name == "produtos:segmento-list"

    def test_create(self) -> None:
        assert reverse("produtos:segmento-create") == "/produtos/segmentos/create/"
        assert (
            resolve("/produtos/segmentos/create/").view_name
            == "produtos:segmento-create"
        )

    def test_delete(self, segmento: Segmento) -> None:
        assert (
            reverse("produtos:segmento-delete", args=(segmento.id,))
            == f"/produtos/segmentos/{segmento.id}/delete/"
        )
        assert (
            resolve(f"/produtos/segmentos/{segmento.id}/delete/").view_name
            == "produtos:segmento-delete"
        )


class TestCategoriaUrls:
    def test_detail(self, categoria: Categoria) -> None:
        assert (
            reverse("produtos:categoria-detail", args=(categoria.id,))
            == f"/produtos/categorias/{categoria.id}/"
        )
        assert (
            resolve(f"/produtos/categorias/{categoria.id}/").view_name
            == "produtos:categoria-detail"
        )

    def test_update(self, categoria: Categoria) -> None:
        assert (
            reverse("produtos:categoria-update", args=(categoria.id,))
            == f"/produtos/categorias/{categoria.id}/update/"
        )
        assert (
            resolve(f"/produtos/categorias/{categoria.id}/update/").view_name
            == "produtos:categoria-update"
        )


class TestMarcaUrls:
    def test_detail(self, marca: Marca) -> None:
        assert (
            reverse("produtos:marca-detail", args=(marca.id,))
            == f"/produtos/marcas/{marca.id}/"
        )
        assert (
            resolve(f"/produtos/marcas/{marca.id}/").view_name
            == "produtos:marca-detail"
        )

    def test_update(self, marca: Marca) -> None:
        assert (
            reverse("produtos:marca-update", args=(marca.id,))
            == f"/produtos/marcas/{marca.id}/update/"
        )
        assert (
            resolve(f"/produtos/marcas/{marca.id}/update/").view_name
            == "produtos:marca-update"
        )

    def test_list(self) -> None:
        assert reverse("produtos:marca-list") == "/produtos/marcas/"
        assert resolve("/produtos/marcas/").view_name == "produtos:marca-list"

    def test_create(self) -> None:
        assert reverse("produtos:marca-create") == "/produtos/marcas/create/"
        assert resolve("/produtos/marcas/create/").view_name == "produtos:marca-create"

    def test_delete(self, marca: Marca) -> None:
        assert (
            reverse("produtos:marca-delete", args=(marca.id,))
            == f"/produtos/marcas/{marca.id}/delete/"
        )
        assert (
            resolve(f"/produtos/marcas/{marca.id}/delete/").view_name
            == "produtos:marca-delete"
        )


class TestProdutoUrls:
    def test_detail(self, produto: Produto) -> None:
        assert (
            reverse("produtos:produto-detail", args=(produto.id,))
            == f"/produtos/{produto.id}/"
        )
        assert (
            resolve(f"/produtos/{produto.id}/").view_name == "produtos:produto-detail"
        )

    def test_update(self, produto: Produto) -> None:
        assert (
            reverse("produtos:produto-update", args=(produto.id,))
            == f"/produtos/{produto.id}/update/"
        )
        assert (
            resolve(f"/produtos/{produto.id}/update/").view_name
            == "produtos:produto-update"
        )

    def test_list(self) -> None:
        assert reverse("produtos:produto-list") == "/produtos/"
        assert resolve("/produtos/").view_name == "produtos:produto-list"

    def test_create(self) -> None:
        assert reverse("produtos:produto-create") == "/produtos/create/"
        assert resolve("/produtos/create/").view_name == "produtos:produto-create"

    def test_delete(self, produto: Produto) -> None:
        assert (
            reverse("produtos:produto-delete", args=(produto.id,))
            == f"/produtos/{produto.id}/delete/"
        )
        assert (
            resolve(f"/produtos/{produto.id}/delete/").view_name
            == "produtos:produto-delete"
        )
'''
