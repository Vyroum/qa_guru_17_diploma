import allure
from pages.mobile.app_settings_steps import app_setup
from pages.mobile.catalog_and_cart_steps import catalog, cart
import pytest


@pytest.mark.mobile
@allure.tag("mobile")
class TestMobileApp:
    @allure.tag("precondition")
    @allure.title("Настройка приложения при первом запуске")
    def test_first_launch_setup(self):
        app_setup.skip_start_page()
        app_setup.cancel_geolocation_setting()
        app_setup.choose_city_location("Москва")
        app_setup.close_tutorial_tip()

    @allure.tag("cart", "catalog")
    @allure.title("Добавление предмета в корзину")
    def test_find_item_in_catalog(self):
        app_setup.skip_start_page()
        app_setup.cancel_geolocation_setting()
        app_setup.choose_city_location("Москва")
        app_setup.close_tutorial_tip()
        catalog.searching_item("Пылесос")
        catalog.found_item_confirmation()
        catalog.access_category()
        catalog.add_to_cart()
        cart.open_cart()
        cart.delete_from_cart()


