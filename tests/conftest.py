import pytest
from selene import browser
from selenium import webdriver
import project
import os
from utils import allure_utils



def pytest_addoption(parser):
    parser.addoption(
        "--context",
        action="store",
        default="local",
        help="Context for tests: local/selenoid/emulator/browserstack",
    )

@pytest.fixture
def open_browser():
    browser.open("/")


@pytest.fixture(scope="function", autouse=True)
def browser_set(request):
    context = request.config.getoption("--context")
    os.environ["CONTEXT"] = context
    project_config = project.get_config(context)

    if context == "local":
        browser.config.driver_name = project_config.driver_name
        browser.config.base_url = project_config.base_url
        browser.config.window_width = project_config.window_width
        browser.config.window_height = project_config.window_height
        browser.config.headless = project_config.headless


    elif context == "selenoid":
        from selenium.webdriver import ChromeOptions

        options = ChromeOptions()
        options.set_capability("browserName", project_config.driver_name)
        options.set_capability("browserVersion", project_config.selenoid_browser_version)
        options.set_capability("selenoid:options", {
            "enableVNC": project_config.enable_vnc,
            "enableVideo": project_config.enable_video,
        })

        browser.config.driver = webdriver.Remote(
            command_executor=project_config.selenoid_hub,
            options=options
        )

        browser.config.base_url = project_config.base_url
        browser.config.window_width = project_config.window_width
        browser.config.window_height = project_config.window_height


    elif context in ["emulator", "browserstack"]:
        from appium import webdriver as appium_webdriver
        from appium.options.android import UiAutomator2Options

        browser.config.timeout = 10.0
        desired_caps = {
            "platformName": project_config.platform_name,
            "platformVersion": project_config.platform_version,
            "deviceName": project_config.device_name,
            "automationName": "UiAutomator2"
        }
        if context == "emulator":
            desired_caps["app"] = project_config.app
            command_executor = project_config.appium_hub

        elif context == "browserstack":
            desired_caps.update({
                "app": project_config.bs_app,
                "bstack:options": {
                    "userName": project_config.browserstack_user,
                    "accessKey": project_config.browserstack_key,
                    "projectName": "AllInstruments",
                    "buildName": "Build Test",
                }
            })
            command_executor = project_config.bs_hub

        options = UiAutomator2Options().load_capabilities(desired_caps)

        driver = appium_webdriver.Remote(
            command_executor=command_executor,
            options=options
        )
        browser.config.driver = driver

    yield
    if context in ["local", "selenoid"]:
        allure_utils.attach_screenshot(browser)
        allure_utils.attach_html(browser)
        allure_utils.attach_web_logs(browser)
        allure_utils.attach_video(browser)


    if context in ["local", "selenoid", "emulator", "browserstack"]:
        browser.quit()
