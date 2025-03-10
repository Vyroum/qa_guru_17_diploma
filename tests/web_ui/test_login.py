import allure
from pages.web_ui.login import Login
from resources.common_actions import Common
import pytest


login = Login()
common = Common()

@pytest.mark.web
@allure.story("Манипуляции с логином через браузер")
@allure.title("Проверка неуспешной авторизации")
@allure.tag("login", "web")
def test_failed_authorization():
    common.open_browser()
    login.open_login_form_or_user_page()
    login.input_invalid_login_credentials()
    login.press_login_button()
    login.check_unsuccessfull_authorization()

@pytest.mark.web
@allure.title("Проверка успешной авторизации")
@allure.tag("login", "web")
def test_successfull_authorization():
    common.open_browser()
    login.open_login_form_or_user_page()
    login.input_valid_login_credentials()
    login.press_login_button()
    login.close_tutorial_window()
    login.open_login_form_or_user_page()
    login.check_successul_authorization()


@allure.title("Проверка успешного логаута")
@allure.tag("login", "web")
def test_successfull_logout():
    common.open_browser()
    login.open_login_form_or_user_page()
    login.input_valid_login_credentials()
    login.press_login_button()
    login.close_tutorial_window()
    login.open_login_form_or_user_page()
    login.press_logout_button()
    login.check_successful_logout()
