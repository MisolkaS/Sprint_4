import allure
import pytest
from pages.index_page import IndexPage
from pages.order_page_personal_data import OrderPagePersonalData
class TestNavigation:
    @allure.title('Проверяем, что по клику на логотип Яндекса переходит на страницу Дзена')
    def test_yandex_logo_redirects_to_dzen(self, driver, index_url, expected_url):
        step1 = IndexPage(driver, index_url)
        step1.open_index_page()
        current_url = step1.click_yandex_logo(expected_url)
        assert expected_url in current_url, f"Ожидался URL: {expected_url}, но получен: {current_url}"

    @allure.title('Проверяем, что по клику на логотип Самоката переходит главную страницу')
    def test_logo_redirects_to_index(self, driver, index_url):
        step1 = IndexPage(driver, index_url)
        step1.open_index_page()
        step2 = OrderPagePersonalData(driver)
        step1.click_order_top_or_bottom_button('top')
        step2.click_scooter_logo()
        current_url = driver.current_url
        assert index_url in current_url, f"Ожидался URL: {expected_url}, но получен: {current_url}"



