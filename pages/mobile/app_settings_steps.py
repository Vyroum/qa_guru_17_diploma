import time
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, by, be
from allure import step


class Onboarding:

    def skip_start_page(self):
        with step("Пропуск стартовой страницы"):
            browser.element((AppiumBy.ID, "com.notissimus.allinstruments.android:id/textViewSkip")).click()

    def cancel_geolocation_setting(self):
        with step("Отмена геолокации геолокации"):
            browser.element((AppiumBy.ID, "com.android.packageinstaller:id/permission_deny_button")).click()
        with step("Подтвеждение отмены геолокации"):
            browser.element((AppiumBy.ID, "com.notissimus.allinstruments.android:id/buttonCancel")).click()

    def choose_city_location(self, value):
        with step("Ввод города Москва"):
            browser.element((AppiumBy.ID, "com.notissimus.allinstruments.android:id/editTextSearch")).type(value)
        with step("Выбор города"):
            browser.element((AppiumBy.ID, "com.notissimus.allinstruments.android:id/viewFlipper")).click()

    def close_tutorial_tip(self):
        with step("Закрытие обучающей подсказки"):
            browser.element((AppiumBy.ID, "com.notissimus.allinstruments.android:id/buttonClose")).click()

app_setup = Onboarding()