import allure
import pytest
from pages.web_ui.catalog_page import catalog
from pages.web_ui.cart_page import cart
from resources.cpu import cpu


@pytest.mark.web
@allure.story("Манипуляции с каталогом и корзиной")
class TestCatalogAndCart:
    @allure.title("Поиск товара в каталоге")
    @allure.tag("catalog", "web")
    def test_search_item_in_catalog(self, open_browser):
        catalog.search_product(cpu)
        catalog.check_found_item(cpu)

    @allure.tag("cart", "catalog", "web")
    @allure.title("Добавление предмета в корзину")
    def test_add_item_to_cart(self, open_browser):
        catalog.search_product(cpu)
        catalog.add_to_cart()
        cart.open_cart()
        cart.check_presence_in_cart(cpu)

    @allure.tag("cart", "web")
    @allure.title("Изменение количества предметов в корзине")
    def test_change_item_quantity_in_cart(self, open_browser):
        catalog.search_product(cpu)
        catalog.add_to_cart()
        cart.open_cart()
        cart.check_presence_in_cart(cpu)
        cart.change_quantity_plus_one(cpu)

    @allure.tag("cart", "web")
    @allure.title("Удаление предметов из корзины")
    def test_delete_item_from_cart(self, open_browser):
        catalog.search_product(cpu)
        catalog.add_to_cart()
        cart.open_cart()
        cart.check_presence_in_cart(cpu)
        cart.delete_item_from_cart()
        cart.check_empty_cart()
