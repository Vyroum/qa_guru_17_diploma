import allure
from pages.api.login_api_steps import LoginAPI
from pages.web_ui.login import Login
import pytest

api_login = LoginAPI()
login_action = Login()


@pytest.mark.api
@allure.story("Манипуляция с логином через API")
@allure.tag("api")
@allure.title("Проверка успешной аутентификации через API")
def test_api_successful_authentication():
    api_login.successful_authentication_through_api()
    api_login.check_successful_authorization_in_browser()


@pytest.mark.api
@allure.tag("api")
@allure.title("Проверка аутентификации с ошибкой через API")
def test_api_failed_authentication():
    api_login.failed_authorization_through_api()


@pytest.mark.api
@allure.tag("api")
@allure.title("Проверка логаута через API")
def test_logout_api():
    api_login.successful_authentication_through_api()
    api_login.logout_through_api()
    login_action.check_successful_logout()
