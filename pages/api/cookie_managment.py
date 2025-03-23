import  allure
import requests
from selene import browser
from project import config

class BasketCookieManagment:
    def take_basket_cookie_and_add_to_browser(self, response):
        with allure.step("Получение куки из API"):
            cookie = response.cookies.get("basket_id")

        with allure.step("Добавление куки из API"):
            browser.open('/')
            browser.driver.add_cookie({
                'name': 'basket_id',
                'value': cookie,
                'domain': config.domain_url,
                'path': '/',
                'secure': True,
                'httponly': True
            })
            browser.driver.refresh()

class LoginCookieManager:
    def take_login_cookie_and_add_to_browser(self, response):
        with allure.step("Получение cookie из API"):
            cookie = response.cookies.get("site_laravel_session")

        with allure.step("Добавление cookie из API в сессию браузера"):
            browser.open('/')
            browser.driver.add_cookie({
                'name': 'site_laravel_session',
                'value': cookie,
                'domain': config.login_api_url,
                'path': '/',
                'secure': True,
                'httponly': True
            })
            browser.driver.refresh()


cookie_basket = BasketCookieManagment()
cookie_login = LoginCookieManager()