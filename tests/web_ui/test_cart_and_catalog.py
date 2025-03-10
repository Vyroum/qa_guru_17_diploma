import allure
import pytest
from pages.web_ui.catalog_page import Catalog
from resources.common_actions import Common
from pages.web_ui.cart_page import Cart
from resources.cpu import cpu

common = Common()
catalog = Catalog()
cart = Cart()

@pytest.mark.web
@allure.title("Поиск товара в каталоге")
def test_search_item_in_catalog():
    common.open_browser()
    catalog.search_product_cpu(cpu)
    catalog.check_found_item(cpu)

@pytest.mark.web
@allure.title("Добавление предмета в корзину")
def test_add_item_to_cart():
    common.open_browser()
    catalog.search_product_cpu(cpu)
    catalog.add_to_cart()
    cart.open_cart()
    cart.check_presence_in_cart(cpu)

@pytest.mark.web
@allure.title("Изменение количества предметов в корзине")
def test_change_item_quantity_in_cart():
    common.open_browser()
    catalog.search_product_cpu(cpu)
    catalog.add_to_cart()
    cart.open_cart()
    cart.check_presence_in_cart(cpu)
    cart.change_quantity_plus_one(cpu)

@pytest.mark.web
@allure.title("Удаление предметов из корзины")
def test_delete_item_from_cart():
    common.open_browser()
    catalog.search_product_cpu(cpu)
    catalog.add_to_cart()
    cart.open_cart()
    cart.check_presence_in_cart(cpu)
    cart.delete_item_from_cart()
    cart.check_empty_cart()
