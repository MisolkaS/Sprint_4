from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, page_url):
        self.driver.get(page_url)

    def click_element(self, locator):
        element = self.wait_for_clickable_element(locator)
        element.click()

    def send_keys(self, locator, keys):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(keys)

    def wait_for_elements(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(locator)
        )

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def is_element_present(self, locator):
        try:
            self.wait_for_element(locator)
            return True
        except TimeoutException:
            return False

    def wait_for_clickable_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def get_handle(self):
        return self.driver.current_window_handle

    def wait_for_new_window_and_switch(self, timeout, current_window, expected_url):
        WebDriverWait(self.driver, timeout).until(EC.new_window_is_opened([current_window]))
        for window in self.driver.window_handles:
            if window != current_window:
                self.driver.switch_to.window(window)
                break
        WebDriverWait(self.driver, timeout).until(EC.url_contains(expected_url))
        current_url = self.driver.current_url
        self.driver.close()
        self.driver.switch_to.window(current_window)
        return current_url

    def close_popup_if_present(self, locator):
        try:
            self.wait_for_element(locator, timeout=5)
            close_button = self.driver.find_element(*locator)
            close_button.click()
        except TimeoutException:
            pass

    def enter_text(self, locator, text):
        try:
            input_element = self.wait_for_element(locator)
            input_element.clear()
            input_element.send_keys(text)
        except NoSuchElementException:
            pass

    def enter_text_and_select(self, input_locator, text, option_locator_template):
        try:
            input_element = self.wait_for_clickable_element(input_locator)
            input_element.clear()
            input_element.send_keys(text)
            option_locator = (option_locator_template[0], option_locator_template[1].format(metro=text))

            option = self.wait_for_element(option_locator)
            option.click()
        except NoSuchElementException:
            pass

    def scroll_to(self, element_locator):
        element = self.wait_for_element(element_locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def _question_exists(self, question, locator):
        questions = self.wait_for_elements(locator)
        for q in questions:
            if q.text == question:
                return True
        return False

    def _find_question(self, question, question_locator):
        questions = self.wait_for_elements(question_locator)
        for q in questions:
            if q.text == question:
                return q
        raise NoSuchElementException(f"Вопрос '{question}' не найден.")

    def _click_on_question(self, question, question_locator):
        question_element = self._find_question(question, question_locator)
        question_element.click()

    def _get_answer_text(self, question, question_locator, answer_locator):
        question_element = self._find_question(question, question_locator)
        answer_panel = question_element.find_element(*answer_locator)
        return answer_panel.text
