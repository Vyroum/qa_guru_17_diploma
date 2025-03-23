from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be
from allure import step


class Catalog:

    def searching_item(self, value):
        with step("Поиск товара в каталоге"):
            browser.element((AppiumBy.ID, "com.notissimus.allinstruments.android:id/editTextSearch")).click().type(
                value)

    def found_item_confirmation(self):
        with step("Подтверждение успешного поиска категории 'Пылесосы для дома' и заход в неё"):
            browser.element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Пылесосы для дома")')).should(
                be.visible)
            browser.element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Пылесосы для дома")')).click()

    def access_category(self):
        with step("Заход в подкатегорию 'Вертикальные'"):
            browser.element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Вертикальные").instance(0)')).click()

    def add_to_cart(self):
        with step("Добавление предмета в корзину"):
            browser.element((AppiumBy.ID, "com.notissimus.allinstruments.android:id/buttonPrimaryAction")).click()


class Cart:

    def open_cart(self):
        with step("Открытие корзины"):
            browser.element((AppiumBy.ID, "com.notissimus.allinstruments.android:id/buttonGoToCart")).click()
            with step("Проверка того, что предмет добавлен в корзину"):
                browser.element((AppiumBy.ID, "com.notissimus.allinstruments.android:id/textViewName")).should(
                    have.text("пылесос"))

    def delete_from_cart(self):
        with step("Удаление предмета из корзины"):
            browser.element((AppiumBy.ID, "com.notissimus.allinstruments.android:id/textViewDeleteSelected")).click()
            browser.element((AppiumBy.ID, "com.notissimus.allinstruments.android:id/buttonPositive")).click()
            with step("Проверка удаления из корзины"):
                browser.element((AppiumBy.ID, "com.notissimus.allinstruments.android:id/textViewEmptyTitle")).should(
                    have.text("В корзине пока ничего нет"))


catalog = Catalog()
cart = Cart()
