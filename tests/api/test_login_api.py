import allure
from pages.api.login_api_steps import api_login
from pages.web_ui.login import login_web
import pytest


@pytest.mark.api
@allure.tag("api")
@allure.story("Манипуляция с логином через API")
class TestLoginApi:
    @allure.tag("login")
    @allure.title("Проверка успешной аутентификации через API")
    def test_api_successful_authentication(self):
        api_login.successful_authentication_through_api()
        api_login.check_successful_authorization_in_browser()

    @allure.tag("logout")
    @allure.title("Проверка логаута через API")
    def test_logout_api(self):
        api_login.successful_authentication_through_api()
        api_login.logout_through_api()
        login_web.check_successful_logout()

    @allure.tag("login")
    @allure.title("Проверка аутентификации с ошибкой через API")
    def test_api_failed_authentication(self):
        api_login.failed_authorization_through_api()
        api_login.check_failed_authoriaztion_through_browser()
