import time

from selene import browser, have, by
import allure
from resources.cpu import CPU


class Cart:

    def open_cart(self):
        with allure.step("Открытие корзины"):
            browser.element(by.text("Корзина")).double_click()
            time.sleep(3)

    def check_presence_in_cart(self, value: CPU):
        with allure.step("Проверка наличия предмета в корзине"):
            browser.element("[class='BasketItem_content__HDK_u']").should(have.text(value.model))
            browser.element("[class='CountSwitcher_count__0gn_e']").should(have.value(value.quantity))

    def change_quantity_plus_one(self, value: CPU):
        with allure.step("Изменение количества предметов в корзине (Увеличение на 1)"):
            browser.element("[class='Icons_plus__2Xu2y']").click()
            new_quantity = int(value.quantity) + 1
        with allure.step("Проверка того, что количество предметов изменилось"):
            browser.element("[class='CountSwitcher_count__0gn_e']").should(have.value(str(new_quantity)))

    def delete_item_from_cart(self):
        with allure.step("Удаление предмета из корзины"):
            browser.element("[class='Icons_delete__VMin6 BasketItem_delete___LqNs']").click()

    def check_empty_cart(self):
        with allure.step("Проверка того, что корзина пустая"):
            browser.element("[class='BasketEmpty_black__QhefV']").should(have.text("В корзине пока ничего нет"))


cart = Cart()
