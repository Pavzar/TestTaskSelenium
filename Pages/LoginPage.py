from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Pages.BasePage import BasePage


class LoginPage(BasePage):
    LOGIN_POP_UP_TEXT = (By.XPATH, './/div[@data-role="dialogText"]//strong[text()="Smart-ID"]')
    LOGIN_URL = 'https://www.optibet.lv/login'
    LOGIN_FIELD = (By.XPATH, './/form//child::input[@name="email"]')
    LOGIN_LABEL = (By.XPATH, './/*[@name="email"]//following-sibling::label')
    LOGIN_ERROR_MESSAGE = (By.XPATH, './/*[@name="email"]//following::div[@data-role="validationError"]')

    PASSWORD_FIELD = (By.XPATH, './/form//input[@name="password"]')
    PASSWORD_LABEL = (By.XPATH, './/*[@name="password"]//following::label')
    PASSWORD_ERROR_MESSAGE = (By.XPATH, './/input[@name="password"]//following::div[@data-role="validationError"]')
    HIDE_PASSWORD_ICON = (By.XPATH, './/div[@title="Parādīt paroli"]')
    HIDE_PASSWORD_TEXT = './/form//input[@name="password" and @type="text"]'

    ID_FIELD = (By.XPATH, './/input[@name="personalId"]')
    ID_LABEL = (By.XPATH, './/input[@name="personalId"]//following::label')
    ID_ERROR_MESSAGE = (By.XPATH, './/input[@name="personalId"]//following::div[@data-role="validationError"]')

    SMARTID_BTN = (By.XPATH, '//span[contains(text(),"Smart")]')
    SIGNUP_LINK = (By.LINK_TEXT, 'Pievienojies')
    FORGOT_PASSWORD_LINK = (By.LINK_TEXT, 'Aizmirsi paroli?')

    SUBMIT_BTN = (By.XPATH, './/form//button[@type="submit"]')
    SUBMIT_ID_BTN = (By.XPATH, './/button[@type="submit" and @data-role="loginSubmit"]')

    def __init__(self, driver):
        super().__init__(driver)

    def is_login_popup_appeared(self):
        return self.is_visible(by_locator=self.LOGIN_POP_UP_TEXT)

    def is_login_field_visible(self):
        return self.is_visible(by_locator=self.LOGIN_FIELD)

    def get_login_field_label_text(self):
        return self.get_text_innerhtml(self.LOGIN_LABEL)

    def is_password_field_visible(self):
        return self.is_visible(by_locator=self.PASSWORD_FIELD)

    def is_hide_password_visible(self):
        return self.is_visible(by_locator=self.HIDE_PASSWORD_ICON)

    def get_password_field_label_text(self):
        return self.get_text_innerhtml(self.PASSWORD_LABEL)

    def is_signup_link_visible(self):
        return self.is_visible(by_locator=self.SIGNUP_LINK)

    def is_signup_link_clickable(self):
        return self.is_clickable(by_locator=self.SIGNUP_LINK)

    def is_forgot_password_visible(self):
        return self.is_visible(by_locator=self.FORGOT_PASSWORD_LINK)

    def is_forgot_password_clickable(self):
        return self.is_clickable(by_locator=self.FORGOT_PASSWORD_LINK)

    def is_hide_password_attribute_changed(self):
        self.do_click(by_locator=self.HIDE_PASSWORD_ICON)
        try:
            self.driver.find_element(By.XPATH, self.HIDE_PASSWORD_TEXT)
        except NoSuchElementException:
            return False
        return True

    def is_submit_button_visible(self):
        return self.is_visible(by_locator=self.SUBMIT_BTN)

    def is_submit_button_clickable(self):
        return self.is_clickable(by_locator=self.SUBMIT_BTN)

    def get_submit_button_text(self):
        return self.get_text(self.SUBMIT_BTN)

    def get_login_error_message(self):
        return self.get_text(self.LOGIN_ERROR_MESSAGE)

    def get_login_short_error_message(self):
        return self.get_text()

    def get_password_error_message(self):
        return self.get_text(self.PASSWORD_ERROR_MESSAGE)

    def type_short_login(self):
        self.do_send_keys(self.LOGIN_FIELD, "usern")

    def type_long_login(self):
        self.do_send_keys(self.LOGIN_FIELD, "usernameusernameusernameusernameu")

    def type_symbols_login(self):
        self.do_send_keys(self.LOGIN_FIELD, "u$ername")

    def type_false_login(self):
        self.do_send_keys(self.LOGIN_FIELD, "username")
        self.do_send_keys(self.PASSWORD_FIELD, "123123123")
        self.click_submit()

    def click_submit(self):
        self.do_click(by_locator=self.SUBMIT_BTN)

    def is_id_field_visible(self):
        return self.is_visible(by_locator=self.ID_FIELD)

    def get_id_label_text(self):
        return self.get_text_innerhtml(self.ID_LABEL)

    def type_symbols_id_field(self):
        self.do_send_keys(self.ID_FIELD, "----")

    def get_id_field_error_message(self):
        return self.get_text(self.ID_ERROR_MESSAGE)

    def click_smartid(self):
        self.do_click(by_locator=self.SMARTID_BTN)

    def click_smartid_submit(self):
        self.do_click(by_locator=self.SUBMIT_ID_BTN)

    def type_false_id(self):
        self.do_send_keys(self.ID_FIELD, "99999999999")
