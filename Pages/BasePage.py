import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def check_exists_by_xpath(self, xpath):
        self.driver.implicitly_wait(3)
        try:
            self.driver.find_element(By.XPATH, xpath)
        except NoSuchElementException:
            return False
        return True

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def is_clickable(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator))
        return bool(element)

    def do_clickable_click(self, by_locator):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def if_visible_click(self, by_locator):
        var = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        var.click()

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url

    def switch_from_iframe(self):
        self.driver.switch_to.default_content()

    def switch_to_iframe(self, iframe):
        WebDriverWait(self.driver, 30).until(EC.frame_to_be_available_and_switch_to_it(iframe))

    def get_text_innerhtml(self, xpath):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(xpath)).get_attribute(
            "innerHTML")

    def get_text(self, xpath):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(xpath)).text

