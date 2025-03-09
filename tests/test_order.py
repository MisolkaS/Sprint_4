import pytest
import allure

from helpers import *
from pages.index_page import IndexPage
from pages.order_page_personal_data import OrderPagePersonalData
from pages.order_page_scooter_data import OrderPageScooterData


class TestOrderPositiveCase:
    @pytest.mark.parametrize("user_data", get_test_data())
    @allure.title('Проверяем позитивный сценарий заказа Самоката')
    def test_order_creation_flow_positive_case(self, user_data, driver, index_url):

        step1 = IndexPage(driver, index_url)
        step2 = OrderPagePersonalData(driver)
        step3 = OrderPageScooterData(driver)
        step1.open_index_page()

        step1.close_popup()
        step1.click_order_top_or_bottom_button(user_data["button"])

        step2.enter_name(user_data["name"])
        step2.enter_lastname(user_data["lastname"])
        step2.enter_address(user_data["address"])
        step2.enter_metro(user_data["metro"])
        step2.enter_phone(user_data["phone"])

        step2.click_button_next()

        step3.enter_date(get_random_date())
        step3.enter_period(user_data["period"])
        step3.enter_colors_scooter(user_data["color"])
        step3.enter_comment(user_data["comment"])

        step3.click_button_order()
        step3.click_button_yes_modal_window()
        header_text = step3.check_modal_window_header()

        assert "Заказ оформлен" in header_text





