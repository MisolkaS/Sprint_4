from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import allure

class IndexPage:
    #локатор кнопки заказать вверху страницы
    order_top_button = [By.XPATH, '//div[1]/div[2]/button[1]']

    #локатор кнопки заказать внизу страницы
    order_bottom_button = [By.XPATH, '//div[2]/div[5]/button']

    # локатор кнопки окна Cookie
    popup_close_button = [By.XPATH, "//button[contains(text(), 'да все привыкли')]"]

    # локатор логотипа яндекса
    yandex_logo = [By.CSS_SELECTOR, "a[href='//yandex.ru']"]

    #элемент к которому скролимся
    scroll_to_element_locator = [By.XPATH, "//div[@class='Home_FourPart__1uthg']"]

    #массив кнопок
    accordion_button_locator = [By.XPATH, "//div[@class='accordion__item']"]

    #локатор ответа
    accordion_answer_locator = (By.XPATH, ".//div[@class='accordion__panel']")

    # локатор вопросов
    accordion_question_locator = [By.XPATH, ".//div[@class='accordion__button']"]

    # локатор всплывающего окна
    popup_locator = [By.XPATH, "//button[contains(text(), 'да все привыкли')]"]

    scooter_rental_info = {
        "Сколько это стоит? И как оплатить?": "Сутки — 400 рублей. Оплата курьеру — наличными или картой.",
        "Хочу сразу несколько самокатов! Так можно?": "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.",
        "Как рассчитывается время аренды?": "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.",
        "Можно ли заказать самокат прямо на сегодня?": "Только начиная с завтрашнего дня. Но скоро станем расторопнее.",
        "Можно ли продлить заказ или вернуть самокат раньше?": "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.",
        "Вы привозите зарядку вместе с самокатом?": "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.",
        "Можно ли отменить заказ?": "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.",
        "Я жизу за МКАДом, привезёте?": "Да, обязательно. Всем самокатов! И Москве, и Московской области."
    }


    def __init__(self, driver):
        self.driver = driver

    @allure.step('Нажимаем на кнопку Заказать')
    def click_order_top_or_bottom_button(self, button):
        button_locator = self.order_top_button if button == 'top' else self.order_bottom_button
        self.driver.find_element(*button_locator).click()

    @allure.step('Принимаем Куки')
    def close_popup_if_present(self):
        popups = self.driver.find_elements(*self.popup_locator)
        if popups:
            cookie_button = popups[0]
            cookie_button.click()

    @allure.step('Нажимаем на логотип Яндекса')
    def click_yandex_logo(self):
        current_window = self.driver.current_window_handle
        self.driver.find_element(*self.yandex_logo).click()
        WebDriverWait(self.driver, 10).until(EC.new_window_is_opened([current_window]))
        for window in self.driver.window_handles:
            if window != current_window:
                self.driver.switch_to.window(window)
                break
        time.sleep(3)
        current_url = self.driver.current_url
        self.driver.close()
        self.driver.switch_to.window(current_window)
        return current_url



    @allure.step('Скролим страницу к вопросам')
    def scroll_to_element(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.scroll_to_element_locator)
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Составляем список ответов и вопросов')
    def collect_questions_and_answers(self):
        accordion_items = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.accordion_button_locator)
        )
        qa_pairs = []
        for item in accordion_items:
            question_element = item.find_element(*self.accordion_question_locator)
            question_text = question_element.text
            question_element.click()
            answer_element = WebDriverWait(self.driver, 5).until(
                EC.visibility_of(item.find_element(*self.accordion_answer_locator))
            )
            answer_text = answer_element.text
            qa_pairs.append((question_text, answer_text))
        return qa_pairs
