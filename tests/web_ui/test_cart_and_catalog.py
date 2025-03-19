import allure
import pytest
from pages.web_ui.catalog_page import Catalog
from pages.web_ui.cart_page import Cart
from resources.cpu import cpu

catalog = Catalog()
cart = Cart()


@pytest.mark.web
@allure.story("Манипуляции с каталогом и корзиной")
@allure.title("Поиск товара в каталоге")
@allure.tag("catalog", "web")
def test_search_item_in_catalog(open_browser):
    catalog.search_product(cpu)
    catalog.check_found_item(cpu)


@pytest.mark.web
@allure.title("Добавление предмета в корзину")
@allure.tag("cart", "catalog", "web")
def test_add_item_to_cart(open_browser):
    catalog.search_product(cpu)
    catalog.add_to_cart()
    cart.open_cart()
    cart.check_presence_in_cart(cpu)


@pytest.mark.web
@allure.title("Изменение количества предметов в корзине")
@allure.tag("cart", "web")
def test_change_item_quantity_in_cart(open_browser):
    catalog.search_product(cpu)
    catalog.add_to_cart()
    cart.open_cart()
    cart.check_presence_in_cart(cpu)
    cart.change_quantity_plus_one(cpu)


@pytest.mark.web
@allure.tag("cart", "web")
@allure.title("Удаление предметов из корзины")
def test_delete_item_from_cart(open_browser):
    catalog.search_product(cpu)
    catalog.add_to_cart()
    cart.open_cart()
    cart.check_presence_in_cart(cpu)
    cart.delete_item_from_cart()
    cart.check_empty_cart()
