import allure
from locators import OrderPagePersonalDataLocators
from pages.base_page import BasePage
class OrderPagePersonalData(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderPagePersonalDataLocators()


    @allure.step('Вводим Имя')
    def enter_name(self, name):
        self.enter_text(self.locators.NAME_INPUT, name)

    @allure.step('Вводим Фамилию')
    def enter_lastname(self, lastname):
        self.enter_text(self.locators.LASTNAME_INPUT, lastname)

    @allure.step('Вводим Адрес')
    def enter_address(self, address):
        self.enter_text(self.locators.ADDRESS_INPUT, address)

    @allure.step('Вводим Станцию метро')
    def enter_metro(self, metro):
        self.enter_text_and_select(self.locators.METRO_INPUT, metro, self.locators.METRO_OPTION)

    @allure.step('Вводим Телефон')
    def enter_phone(self, phone):
        self.enter_text(self.locators.PHONE_INPUT, phone)

    @allure.step('Нажимаем кнопку Далее')
    def click_button_next(self):
        self.click_element(self.locators.NEXT_BUTTON)

    @allure.step('Нажимаем на логотип Самоката')
    def click_scooter_logo(self):
        self.click_element(self.locators.SCOOTER_LOGO)
