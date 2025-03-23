import os
from dotenv import load_dotenv
from selene import browser, have, by, be
import allure

load_dotenv(".env.site_credentials")
email = os.getenv("email")
password = os.getenv("password")

class Login:
    def open_login_form_or_user_page(self):
        with allure.step("Открытие формы логина или личного кабинета"):
            browser.element(by.text("Кабинет")).click()

    def check_login_form(self):
        with allure.step("Проверка формы логина"):
            browser.element(by.text("Личный кабинет")).should(be.visible)

    def input_valid_login_credentials(self):
        with allure.step("Ввод валидного логина и пароля"):

            browser.element(by.name("login")).click().type(email)
            browser.element(by.name("password")).click().type(password)



    def input_invalid_login_credentials(self):
        with allure.step("Ввод невалидного логина и пароля"):
            browser.element(by.name("login")).click().type("1231421@13212.ru")
            browser.element(by.name("password")).click().type("123125412")


    def press_login_button(self):
        with allure.step("Нажатие кнопки войти"):
            browser.element(by.text("Войти")).click()

    def close_tutorial_window(self):
        with allure.step("Закрытие обучающего окна"):
            browser.element(by.class_name("OnboardingScene_closeBtn__tc4rN")).click()

    def check_successul_authorization(self):
        with allure.step("Проверка успешной авторизации под использованным логином"):
            browser.element(by.class_name("sticky-outer-wrapper")).should(have.text(email))

    def check_unsuccessfull_authorization(self):
        with allure.step("Проверка неудачной авторизации"):
            browser.element('[id="AUTHORIZATION_MODAL_WRAPPER"]').should(have.text("Некорректный e-mail или пароль"))

    def press_logout_button(self):
        with allure.step("Нажатие на кнопку выхода из аккаунта"):
            browser.element("[class='Icons_logout__kYaZG SideUser_logoutIcon__K92Iu']").click()

    def check_successful_logout(self):
        with allure.step("Открытие формы логина и проверка успешного логаута"):
            browser.element(by.text("Кабинет")).click()
            browser.element(by.name("login")).should(be.visible)
            browser.element(by.name("password")).should(be.visible)

login_web = Login()