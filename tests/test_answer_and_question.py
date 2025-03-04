from selenium import webdriver
from pages.index_page import IndexPage
import allure


class TestAnswerAndQuestion:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.index_url = "https://qa-scooter.praktikum-services.ru"

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    @allure.description('Проверяем, что все вопросы содержат правильные ответы')
    def test_click(self):
        self.driver.get(self.index_url)
        step1 = IndexPage(self.driver)
        step1.close_popup_if_present()
        step1.scroll_to_element()
        questions_and_answers = step1.collect_questions_and_answers()

        for question, answer in questions_and_answers:
            expected_answer = step1.scooter_rental_info.get(question)
            assert answer == expected_answer, f"Ответ на вопрос '{question}' не соответствует ожидаемому."

