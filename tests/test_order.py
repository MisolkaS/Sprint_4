import allure
import pytest
from selenium import webdriver

import random

from datetime import datetime, timedelta

from pages.index_page import IndexPage
from pages.order_page_personal_data import OrderPagePersonalData
from pages.order_page_scooter_data import OrderPageScooterData

class TestOrderPositiveCase:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.index_url = "https://qa-scooter.praktikum-services.ru"

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    @staticmethod
    def get_random_date():
        start_date = datetime.now() + timedelta(days=1)
        end_date = start_date + timedelta(days=7)
        random_date = start_date + (end_date - start_date) * random.random()
        return random_date.strftime("%d.%m.%Y")

    @staticmethod
    def get_test_data():
        return [
            {
                "name": "Алина",
                "lastname": "Ситалова",
                "address": "Улица Планерная, 1",
                "metro": "Черкизовская",
                "phone": "79312312311",
                "date": None,
                "period": "сутки",
                "color": ["grey", "black"],
                "comment": "Позвоните в домофон",
                "button": "top"
            },
            {
                "name": "София",
                "lastname": "Прекрасная",
                "address": "Улица Пушкина, 2",
                "metro": "Арбатская",
                "phone": "89312312311",
                "date": None,
                "period": "пятеро суток",
                "color": ["grey"],
                "comment": "Позвоните за час",
                "button": "bottom"
            }
        ]

    @allure.description('Проверяем позитивный сценарий заказа Самоката')
    @pytest.mark.parametrize("user_data", get_test_data())
    def test_order_creation_flow_positive_case(self, user_data):
        self.driver.get(self.index_url)

        step1 = IndexPage(self.driver)
        step2 = OrderPagePersonalData(self.driver)
        step3 = OrderPageScooterData(self.driver)

        step1.close_popup_if_present()
        step1.click_order_top_or_bottom_button(user_data["button"])

        step2.enter_name(user_data["name"])
        step2.enter_lastname(user_data["lastname"])
        step2.enter_address(user_data["address"])
        step2.enter_metro(user_data["metro"])
        step2.enter_phone(user_data["phone"])

        step2.click_button_next()

        step3.enter_date(self.get_random_date())
        step3.enter_period(user_data["period"])
        step3.enter_colors_scooter(user_data["color"])
        step3.enter_comment(user_data["comment"])

        step3.click_button_order()
        step3.click_button_yes_modal_window()
        header_text = step3.check_modal_window_header()

        assert "Заказ оформлен" in header_text





