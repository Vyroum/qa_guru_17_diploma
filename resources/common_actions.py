import allure
from selene import browser


class Common:
    def open_browser(self):
        with allure.step("Открываем браузер"):
            browser.open("/")