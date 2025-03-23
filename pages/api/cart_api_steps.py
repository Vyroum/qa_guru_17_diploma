import requests
from selene import browser
import allure
from pages.web_ui.cart_page import cart
from pages.api.cookie_managment import cookie_basket

from resources.cpu import cpu
from project import config

header1 = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"}
payload1 = {
    "goods": [
        {
            "good_id": 411819,
            "good_count": 1
        }
    ]
}


class CartAPI:

    def add_item_to_cart_though_api(self):
        with allure.step("Запрос на добавление предмета в корзину"):
            r = requests.put(f'{config.base_url}api/site/basket', json=payload1, headers=header1)
            assert r.status_code == 200

            cookie_basket.take_basket_cookie_and_add_to_browser(r)

    def delete_item_from_cart(self):
        with allure.step("Запрос на добавление предмета в корзину"):
            r = requests.put(f'{config.base_url}api/site/basket', json=payload1, headers=header1)
            assert r.status_code == 200


            cookie_basket.take_basket_cookie_and_add_to_browser(r)
        with allure.step("Проверка успешного добавления в корзину"):
            cart.open_cart()
            cart.check_presence_in_cart(cpu)

        with allure.step("Запрос на очистку корзины"):
            r = requests.delete(f'{config.base_url}api/site/basket')
            assert r.status_code == 200


        # Механизм очистки корзины просто очищает куки
        # Поэтому вместо взятия удаленного куки выполняется удаление куки
        with allure.step("Очистка куки корзины"):
            browser.driver.delete_cookie("basket_id")
            browser.driver.refresh()

cart_api = CartAPI