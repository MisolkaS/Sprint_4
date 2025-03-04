from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import allure

class OrderPageScooterData:
    # локатор поля когда привезти самокат
    date_input_locator = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"]

    # Локатор для пользовательского выпадающего списка "Срок аренды"
    period_input = [By.XPATH, "//div/div[2]/div[2]/div[2]"]


    # локатор Поля черный цвет самоката
    color_black_input = [By.ID, '//*@id=black']

    # локатор Поля серый цвет самоката
    color_grey_input = [By.ID, '//*@id=grey']

    # локатор поля Комментарий для курьера
    comment_input = [By.XPATH, "//input[@placeholder='Комментарий для курьера']"]

    # локатор кнопки Заказать
    order_button = [By.XPATH, "//div/div[2]/div[3]/button[text()='Заказать']"]
    before_button = [By.XPATH, "//button[text()='Назад']"]


    modal_window = (By.XPATH, '//div[@class="Order_Modal__YZ-d3"]')
    modal_window_header = [By.XPATH, '//div[@class="Order_ModalHeader__3FDaJ"]']
    modal_window_yes = [By.XPATH, "//button[text()='Да']"]

    dropdown_option_locator = [By.CLASS_NAME, 'Dropdown-option']
    body_locator = [By.TAG_NAME, 'body']
    black_locator = [By.ID, "black"]
    grey_locator = [By.ID, "grey"]

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Вводим Дату')
    def enter_date(self, date):
        date_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.date_input_locator)
        )
        date_input.clear()
        date_input.send_keys(date)
        date_input.send_keys(Keys.RETURN)

    @allure.step('Вводим Период')
    def enter_period(self, period):
        self.driver.find_element(*self.body_locator).click()
        dropdown = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.period_input)
        )
        dropdown.click()
        options = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((self.dropdown_option_locator))
        )

        for option in options:
            if option.text == period:
                option.click()
                break

    @allure.step('Вводим цвет самоката')
    def enter_colors_scooter(self, colors):
        for color in colors:
            if color == "black":
                checkbox = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((self.black_locator))
                )
                checkbox.click()
            elif color == "grey":
                checkbox = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((self.grey_locator))
                )
                checkbox.click()

    @allure.step('Вводим Комментарий')
    def enter_comment(self, comment):
        self.driver.find_element(*self.comment_input).send_keys(comment)

    @allure.step('Нажимаем кнопку Заказать')
    def click_button_order(self):
        self.driver.find_element(*self.order_button).click()

    @allure.step('Нажимаем кнопку Назад')
    def click_button_before(self):
        self.driver.find_element(*self.before_button).click()

    @allure.step('Подтверждаем заказ')
    def click_button_yes_modal_window(self):
        self.driver.find_element(*self.modal_window_yes).click()

    @allure.step('Проверяем заголовок модального окна')
    def check_modal_window_header(self):
        header = self.driver.find_element(*self.modal_window_header)
        return header.text





