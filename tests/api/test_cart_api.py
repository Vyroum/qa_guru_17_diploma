import allure
from pages.api.cart_api_steps import cart_api
from pages.web_ui.cart_page import cart
from resources.cpu import cpu
import pytest


@allure.story("Манипуляции с корзиной через API")
@pytest.mark.api
@allure.tag("api", "cart")
class TestCartApi:

    @allure.title("Добавление предмета в корзину через API и проверка в браузере")
    def test_add_item_to_cart_api(self):
        cart_api.add_item_to_cart_though_api(cpu)
        cart.open_cart()
        cart.check_presence_in_cart(cpu)

    @allure.title("Удаление предмета из корзины через API и проверка в браузере")
    def test_delete_item_from_cart(self):
        cart_api.delete_item_from_cart(cpu)
        cart.open_cart()
        cart.check_empty_cart()
