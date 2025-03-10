import allure
from pages.api.cart_api_steps import CartAPI
from pages.web_ui.cart_page import Cart
from resources.cpu import cpu
import pytest

cart = Cart()
cart_api = CartAPI()

@allure.story("Манипуляции с корзиной через API")
@pytest.mark.api
@allure.tag("api")
@allure.title("Добавление предмета в корзину через API и проверка в браузере")
def test_add_item_to_cart_api():
    cart_api.add_item_to_cart_though_api()
    cart.open_cart()
    cart.check_presence_in_cart(cpu)

@pytest.mark.api
@allure.title("Удаление предмета из корзины через API и проверка в браузере")
def test_delete_item_from_cart():
    cart_api.delete_item_from_cart()
    cart.open_cart()
    cart.check_empty_cart()
