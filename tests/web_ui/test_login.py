import allure
from pages.web_ui.login import login_web

import pytest


@pytest.mark.web
@allure.story("Взаимодействие с логином через веб-интерфейс")
class TestWebLogin:
    @allure.title("Проверка успешной авторизации")
    @allure.tag("login", "web")
    def test_successfull_authorization(self, open_browser):
        login_web.open_login_form_or_user_page()
        login_web.input_valid_login_credentials()
        login_web.press_login_button()
        login_web.close_tutorial_window()
        login_web.open_login_form_or_user_page()
        login_web.check_successul_authorization()

    @allure.title("Проверка успешного логаута")
    @allure.tag("login", "web")
    def test_successfull_logout(self, open_browser):
        login_web.open_login_form_or_user_page()
        login_web.input_valid_login_credentials()
        login_web.press_login_button()
        login_web.close_tutorial_window()
        login_web.open_login_form_or_user_page()
        login_web.press_logout_button()
        login_web.check_successful_logout()

    @allure.title("Проверка неуспешной авторизации")
    @allure.tag("login", "web")
    def test_failed_authorization(self, open_browser):
        login_web.open_login_form_or_user_page()
        login_web.input_invalid_login_credentials()
        login_web.press_login_button()
        login_web.check_unsuccessfull_authorization()
