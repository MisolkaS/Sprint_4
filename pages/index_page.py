import allure
from locators import IndexPageLocators
from pages.base_page import BasePage
class IndexPage(BasePage):
    def __init__(self, driver, index_url):
        super().__init__(driver)
        self.index_url = index_url
        self.locators = IndexPageLocators()

    def open_index_page(self):
        self.open_page(self.index_url)

    def click_element(self, locator):
        element = self.wait_for_element(locator)
        element.click()

    @allure.step("Кликаем на кнопку 'Заказать'")
    def click_order_top_or_bottom_button(self, button):
        button_locator = self.locators.ORDER_TOP_BUTTON if button == 'top' else self.locators.ORDER_BOTTOM_BUTTON
        self.click_element(button_locator)

    @allure.step("Закрываем всплывающее окно")
    def close_popup(self):
        self.close_popup_if_present(self.locators.POPUP_LOCATOR)

    @allure.step("Кликаем на логотип Яндекса и переключаемся на новую вкладку")
    def click_yandex_logo(self, expected_url):
        current_window = self.get_handle()
        self.click_element(self.locators.YANDEX_LOGO)
        current_url = self.wait_for_new_window_and_switch(20, current_window, expected_url)
        return current_url

    @allure.step("Переключаем аккордеон для вопроса с индексом {question_index}")
    def toggle_question(self, question_index):
        question_locator = self.locators.QUESTION_ACCORDION.format(question_index)
        self.click(question_locator)

    @allure.step("Кликаем по вопросу с индексом {question_index}")
    def click_question(self, question_index):
        question_locator = self.locators.QUESTION_ITEM.format(question_index)
        self.click(question_locator)

    @allure.step("Получаем текст ответа на вопрос с индексом {question_index}")
    def get_answer_text(self, question_index):
        answer_locator = self.locators.ANSWER_TEXT.format(question_index)
        return self.get_text(answer_locator)

    @allure.step("Прокручиваем страницу к элементу")
    def scroll_to_element(self):
        self.scroll_to(self.locators.SCROLL_TO_ELEMENT_LOCATOR)

    @allure.step("Проверяем существование вопроса: {question}")
    def question_exists(self, question):
        return self._question_exists(question, self.locators.ACCORDION_BUTTON_LOCATOR)

    @allure.step("Кликаем по вопросу: {question}")
    def click_on_question(self, question):
        self._click_on_question(question, self.locators.ACCORDION_QUESTION_LOCATOR)

    @allure.step("Получаем текст ответа на вопрос: {question}")
    def get_answer_text(self, question):
        return self._get_answer_text(question, self.locators.ACCORDION_QUESTION_LOCATOR, self.locators.ANSWER_LOCATOR)