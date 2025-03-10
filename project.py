import dotenv
import pydantic_settings
from typing import Literal, Optional
import os

from selene.support.shared import config

APP_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "resources", "vse_instrumenti.apk"))

class Config(pydantic_settings.BaseSettings):
    # Контекст запуска: local/selenoid/emulator/browserstack
    context: Literal["local", "selenoid", "emulator", "browserstack"] = "local"

    # Общие настройки для WEB/API
    base_url: str = "https://www.regard.ru/"
    domain_url: str = "www.regard.ru"
    login_api_url: str = ".www.regard.ru"
    timeout: float = 3.0

    # Локальный/Selenoid (WEB)
    driver_name: str = "chrome"
    email: str = ""
    password: str = ""
    window_width: int = 1920
    window_height: int = 1080
    headless: bool = False
    selenoid_user: str = ""
    selenoid_password: str = ""
    @property
    def selenoid_hub(self) -> str:
        return f"https://{self.selenoid_user}:{self.selenoid_password}@selenoid.autotests.cloud/wd/hub"
    selenoid_browser_version: Optional[str] = "100.0"
    enable_vnc: bool = False
    enable_video: bool = False

    # Мобильные тесты (Appium)
    appium_hub: Optional[str] = None  # Пример: http://localhost:4723/wd/hub
    bs_hub: Optional[str] = None
    platform_name: Optional[str] = None  # Android/iOS
    platform_version: Optional[str] = None  # 11.0, 14.0 и т.д.
    device_name: Optional[str] = None  # emulator-5554, iPhone 12 и т.д.
    app: Optional[str] = APP_PATH  # Путь к APK/IPA или BrowserStack ID
    bs_app: Optional[str] = None
    browserstack_user: Optional[str] = None
    browserstack_key: Optional[str] = None


def get_config(context: str) -> Config:
    dotenv.load_dotenv(dotenv.find_dotenv(f".env.{context}"))
    return Config()
config = Config()