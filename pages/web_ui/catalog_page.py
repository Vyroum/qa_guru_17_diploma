import time

from selene import browser, have, by
import allure
from resources.cpu import CPU


class Catalog:

    def search_product_cpu(self, value: CPU):
        with allure.step("Поиск процессора Intel Core i7"):
            browser.element("[id='searchInput']").click().type(value.model).press_enter()
            time.sleep(2)

    def check_found_item(self, value: CPU):
        with allure.step("Проверка успешного поиска"):
            browser.element("[class='rendererWrapper']").should(have.text(value.model))

    def add_to_cart(self):
        with allure.step("Добавление предмета в корзину"):
            browser.element(by.text("В корзину")).click()
            time.sleep(2)
