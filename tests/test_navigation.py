import allure
from selenium import webdriver
from pages.index_page import IndexPage
from pages.order_page_personal_data import OrderPagePersonalData


class TestNavigation:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.index_url = "https://qa-scooter.praktikum-services.ru"

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    @allure.description('Проверяем, что по клику на логотип Яндекса переходит на страницу Дзена')
    def test_yandex_logo_redirects_to_dzen(self):
        self.driver.get(self.index_url)
        step1 = IndexPage(self.driver)

        current_url = step1.click_yandex_logo()
        expected_url = "https://dzen.ru"
        assert expected_url in current_url, f"Ожидался URL: {expected_url}, но получен: {current_url}"

    @allure.description('Проверяем, что по клику на логотип Самоката переходит главную страницу')
    def test_logo_redirects_to_index(self):
        self.driver.get(self.index_url)
        step1 = IndexPage(self.driver)
        step2 = OrderPagePersonalData(self.driver)

        step1.click_order_top_or_bottom_button('top')
        step2.click_scooter_logo()
        current_url = self.driver.current_url

        assert self.index_url in current_url, f"Ожидался URL: {expected_url}, но получен: {current_url}"



