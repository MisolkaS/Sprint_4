import allure
import pytest
from pages.index_page import IndexPage
from data import *
class TestQuestionAnswer:
    @pytest.mark.parametrize("question", scooter_rental_info.keys())
    @allure.title('Проверяем соответствие вопросов и ответов')
    def test_faq_answers(self, question, driver, index_url):
        aq_page = IndexPage(driver, index_url)
        aq_page.open_index_page()
        aq_page.scroll_to_element()
        assert aq_page.question_exists(question), f"Вопрос '{question}' не найден на странице."

        aq_page.click_on_question(question)
        answer_text = aq_page.get_answer_text(question)
        expected_answer = scooter_rental_info[question]
        assert answer_text == expected_answer, f"Ответ не совпадает для вопроса: {question}"