from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class OrderPagePersonalData:
    # локатор поля Имя
    name_input = [By.XPATH, '//div[2]/div[2]/div[1]/input']

    # локатор поля Фамилия
    lastname_input = [By.XPATH, '//div[2]/div[2]/div[2]/input']

    # локатор Поля Адрес: куда привезти заказ
    address_input = [By.XPATH, '//div[2]/div[2]/div[3]/input']

    # локатор поля Станция метро
    metro_input = [By.CSS_SELECTOR, '.select-search__input']

    # локатор поля Телефон
    phone_input = [By.XPATH, '//div[2]/div[2]/div[5]/input']

    # локатор кнопки Далее
    next_button = [By.XPATH, '//div[2]/div[3]/button']

    # локатор логотипа Самоката
    scooter_logo = [By.CSS_SELECTOR, "a[href='/']"]


    def __init__(self, driver):
        self.driver = driver

    @allure.step('Вводим Имя')
    def enter_name(self, name):
        self.driver.find_element(*self.name_input).send_keys(name)

    @allure.step('Вводим Фамилию')
    def enter_lastname(self, lastname):
        self.driver.find_element(*self.lastname_input).send_keys(lastname)

    @allure.step('Вводим Адрес')
    def enter_address(self, address):
        self.driver.find_element(*self.address_input).send_keys(address)

    @allure.step('Вводим Станцию метро')
    def enter_metro(self, metro):
        input_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((self.metro_input))
        )
        input_element.clear()
        input_element.send_keys(metro)
        option = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, f"//div[contains(text(), '{metro}')]"))
        )
        option.click()

    @allure.step('Вводим Телефон')
    def enter_phone(self, phone):
        self.driver.find_element(*self.phone_input).send_keys(phone)

    @allure.step('Нажимаем кнопку Далее')
    def click_button_next(self):
        self.driver.find_element(*self.next_button).click()

    @allure.step('Нажимаем на логотип Самоката')
    def click_scooter_logo(self):
        self.driver.find_element(*self.scooter_logo).click()


