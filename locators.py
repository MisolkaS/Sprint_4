from selenium.webdriver.common.by import By
class OrderScooterPageLocators:
    # Локаторы для страницы заказа самоката

    # Поле ввода даты, когда нужно привезти самокат
    DATE_INPUT_LOCATOR = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")

    # Поле выбора периода
    PERIOD_INPUT_LOCATOR = (
    By.XPATH, "//div[contains(@class, 'Dropdown-root')]//div[contains(@class, 'Dropdown-control')]")

    # Поле ввода комментария для курьера
    COMMENT_INPUT_LOCATOR = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")

    # Кнопка для подтверждения заказа
    ORDER_BUTTON_LOCATOR = (By.XPATH, "//button[contains(@class, 'Button_Middle__1CSJM') and text()='Заказать']")

    # Кнопка для возврата на предыдущую страницу
    BEFORE_BUTTON_LOCATOR = (By.XPATH, "//button[text()='Назад']")

    # Кнопка 'Да' в модальном окне подтверждения
    MODAL_WINDOW_YES_LOCATOR = (By.XPATH, "//button[text()='Да']")

    # Заголовок модального окна
    MODAL_WINDOW_HEADER_LOCATOR = (By.XPATH, '//div[@class="Order_ModalHeader__3FDaJ"]')

    # Опция выбора в выпадающем списке
    DROPDOWN_OPTION_LOCATOR = (By.CLASS_NAME, 'Dropdown-option')

    # Локатор для всего тела страницы
    BODY_LOCATOR = (By.TAG_NAME, 'body')

    # Локатор для черного цвета самоката
    BLACK_LOCATOR = (By.ID, "black")

    # Локатор для серого цвета самоката
    GREY_LOCATOR = (By.ID, "grey")


class IndexPageLocators:
    # Локаторы кнопок "Заказать"
    ORDER_TOP_BUTTON = [By.XPATH, "//div[@class='Header_Nav__AGCXC']/button[contains(text(), 'Заказать')]"]
    ORDER_BOTTOM_BUTTON = [By.XPATH, "//div[@class='Home_FinishButton__1_cWm']/button[contains(text(), 'Заказать')]"]

    # Локатор кнопки закрытия окна Cookie
    POPUP_CLOSE_BUTTON = [By.XPATH, "//button[contains(text(), 'да все привыкли')]"]

    # Локатор логотипа Яндекса
    YANDEX_LOGO = [By.CSS_SELECTOR, "a[href='//yandex.ru']"]

    # Элемент, к которому скролимся
    SCROLL_TO_ELEMENT_LOCATOR = [By.XPATH, "//div[@class='Home_FourPart__1uthg']"]

    # Локаторы аккордеонов
    ACCORDION_BUTTON_LOCATOR = [By.XPATH, "//div[@class='accordion__item']"]
    ACCORDION_ANSWER_LOCATOR = [By.XPATH, ".//div[@class='accordion__panel']"]
    ACCORDION_QUESTION_LOCATOR = [By.XPATH, ".//div[@class='accordion__button']"]
    ANSWER_LOCATOR= (By.XPATH, '../following-sibling::div[@role="region"]')

    # Локатор всплывающего окна
    POPUP_LOCATOR = [By.XPATH, "//button[contains(text(), 'да все привыкли')]"]

class OrderPagePersonalDataLocators:
    # Локатор поля Имя
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")

    # Локатор поля Фамилия
    LASTNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")

    # Локатор поля Адрес: куда привезти заказ
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")

    METRO_INPUT = (By.CSS_SELECTOR, '.select-search__input')  # Локатор для поля ввода метро
    METRO_OPTION = (By.XPATH, "//div[contains(text(), '{metro}')]")

    # Локатор поля Телефон
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")

    # Локатор кнопки Далее
    NEXT_BUTTON = (By.XPATH, "//div[@class='Order_NextButton__1_rCA']//button[text()='Далее']")

    # Локатор логотипа Самоката
    SCOOTER_LOGO = (By.CSS_SELECTOR, "a[href='/']")

