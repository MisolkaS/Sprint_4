import allure
from locators import OrderScooterPageLocators
from pages.base_page import BasePage


class OrderPageScooterData(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderScooterPageLocators()

    @allure.step('Вводим Дату')
    def enter_date(self, date):
        self.send_keys(self.locators.DATE_INPUT_LOCATOR, date)

    @allure.step('Вводим Период')
    def enter_period(self, period):
        self.click_element(self.locators.BODY_LOCATOR)
        self.click_element(self.locators.PERIOD_INPUT_LOCATOR)
        options = self.wait_for_elements(self.locators.DROPDOWN_OPTION_LOCATOR)

        for option in options:
            if option.text == period:
                option.click()
                break

    @allure.step('Вводим цвет самоката')
    def enter_colors_scooter(self, colors):
        for color in colors:
            if color == "black":
                self.click_element(self.locators.BLACK_LOCATOR)
            elif color == "grey":
                self.click_element(self.locators.GREY_LOCATOR)

    @allure.step('Вводим Комментарий')
    def enter_comment(self, comment):
        self.send_keys(OrderScooterPageLocators.COMMENT_INPUT_LOCATOR, comment)

    @allure.step('Нажимаем кнопку Заказать')
    def click_button_order(self):
        self.click_element(self.locators.ORDER_BUTTON_LOCATOR)

    @allure.step('Нажимаем кнопку Назад')
    def click_button_before(self):
        self.click_element(self.locators.BEFORE_BUTTON_LOCATOR)

    @allure.step('Подтверждаем заказ')
    def click_button_yes_modal_window(self):
        self.click_element(self.locators.MODAL_WINDOW_YES_LOCATOR)

    @allure.step('Проверяем заголовок модального окна')
    def check_modal_window_header(self):
        header = self.wait_for_element(self.locators.MODAL_WINDOW_HEADER_LOCATOR)
        return header.text