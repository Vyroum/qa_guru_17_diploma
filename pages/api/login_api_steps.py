import time
import requests
from dotenv import load_dotenv

import allure
from jsonschema import validate
import os
from pages.web_ui.login import login_web
from pages.api.cookie_managment import cookie_login
from resources.schema import login_schema
from allure_commons.types import AttachmentType
from project import config

load_dotenv(".env.site_credentials")
email = os.getenv("email")
password = os.getenv("password")
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36'
}


class LoginAPI:

    def successful_authentication_through_api(self):
        with allure.step('Запрос на авторизацию с валидными данными'):
            time.sleep(1)
            r = requests.post(f'{config.base_url}api/site/login/',
                              data={"login": email, "password": password},
                              allow_redirects=False, headers=headers)
        with allure.step("Проверка статус кода"):
            assert r.status_code == 200
            body = r.json()
        with allure.step("Валидация JSON-схемы ответа"):
            validate(body, login_schema)

            cookie_login.take_login_cookie_and_add_to_browser(r)

            allure.attach(body=r.url, name="Request URL", attachment_type=AttachmentType.TEXT, extension="txt")
            allure.attach(body=r.text, name="Response", attachment_type=AttachmentType.TEXT, extension="txt")
            allure.attach(body=str(r.status_code), name="Status Code", attachment_type=AttachmentType.TEXT,
                          extension="txt")

    def check_successful_authorization_in_browser(self):
        with allure.step("Проверка успешной авторизации в браузере"):
            login_web.close_tutorial_window()
            login_web.open_login_form_or_user_page()
            login_web.check_successul_authorization()

    def failed_authorization_through_api(self):
        with allure.step("Запрос на авторизацию с невалидными данными"):
            time.sleep(1)
            r = requests.post(f'{config.base_url}api/site/login/',
                              data={"login": "1231@awfwa.ru", "password": "awgagawg"}, allow_redirects=True)
        with allure.step("Проверка статус кода"):
            assert r.status_code == 401
            cookie_login.take_login_cookie_and_add_to_browser(r)
            allure.attach(body=r.url, name="Request URL", attachment_type=AttachmentType.TEXT, extension="txt")
            allure.attach(body=r.text, name="Response", attachment_type=AttachmentType.TEXT, extension="txt")
            allure.attach(body=str(r.status_code), name="Status Code", attachment_type=AttachmentType.TEXT,
                          extension="txt")
            time.sleep(1)

    def check_failed_authoriaztion_through_browser(self):
        login_web.open_login_form_or_user_page()
        login_web.check_login_form()

    def logout_through_api(self):
        with allure.step("Запрос на логаут через API"):
            r = requests.get(f'{config.base_url}profile/logout',
                             data={"login": email, "password": password},
                             allow_redirects=False, headers=headers)
        with allure.step("Проверка статус кода"):
            assert r.status_code == 302
            allure.attach(body=r.url, name="Request URL", attachment_type=AttachmentType.TEXT, extension="txt")
            allure.attach(body=r.text, name="Response", attachment_type=AttachmentType.TEXT, extension="txt")
            allure.attach(body=str(r.status_code), name="Status Code", attachment_type=AttachmentType.TEXT,
                          extension="txt")

            cookie_login.take_login_cookie_and_add_to_browser(r)


api_login = LoginAPI()
