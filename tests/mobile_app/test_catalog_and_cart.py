import time

import allure
from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be
import pytest


@pytest.mark.mobile
@allure.tag("cart", "catalog", "mobile")
@allure.title("Добавление предмета в корзину")
def test_find_item_in_catalog():
    time.sleep(5)
    with step("Пропуск стартовой страницы"):
        browser.element((AppiumBy.ID, "com.notissimus.allinstruments.android:id/textViewSkip")).click()

    with step("Отмена геолокации геолокации"):
        browser.element((AppiumBy.ID, "com.android.packageinstaller:id/permission_deny_button")).click()

    with step("Подтвеждение отмены геолокации"):
        browser.element((AppiumBy.ID, "com.notissimus.allinstruments.android:id/buttonCancel")).click()

    with step("Ввод города Москва"):
        browser.element((AppiumBy.ID, "com.notissimus.allinstruments.android:id/editTextSearch")).type("Москва")

    with step("Выбор города"):
        browser.element((AppiumBy.ID, "com.notissimus.allinstruments.android:id/viewFlipper")).click()

    with step("Закрытие обучающей подсказки"):
        browser.element((AppiumBy.ID, "com.notissimus.allinstruments.android:id/buttonClose")).click()

    with step("Поиск товара в каталоге"):
        browser.element((AppiumBy.ID, "com.notissimus.allinstruments.android:id/editTextSearch")).click().type("Пылесос")
        time.sleep(1)

    with step("Подтверждение успешного поиска категории 'Пылесосы для дома'"):
        browser.element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Пылесосы для дома")')).should(be.visible)
        browser.element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Пылесосы для дома")')).click()
        pass
    with step("Заход в подкатегорию 'Вертикальные'"):
        browser.element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Вертикальные").instance(0)')).click()

    with step("Добавление предмета в корзину"):
        browser.element((AppiumBy.ID, "com.notissimus.allinstruments.android:id/buttonPrimaryAction")).click()

    with step("Открытие корзины"):
        browser.element((AppiumBy.ID, "com.notissimus.allinstruments.android:id/buttonGoToCart")).click()

    with step("Проверка того что предмет добавлен в корзину"):
        browser.element((AppiumBy.ID, "com.notissimus.allinstruments.android:id/textViewName")).should(have.text("пылесос"))

    with step("Удаление предмета из корзины"):
        browser.element((AppiumBy.ID, "com.notissimus.allinstruments.android:id/textViewDeleteSelected")).click()
        browser.element((AppiumBy.ID, "com.notissimus.allinstruments.android:id/buttonPositive")).click()

    with step("Проверка удаления из корзины"):
        browser.element((AppiumBy.ID, "com.notissimus.allinstruments.android:id/textViewEmptyTitle")).should(have.text("В корзине пока ничего нет"))



