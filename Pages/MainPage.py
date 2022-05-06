from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage
from Pages.CasinoPage import CasinoPage
from Pages.RegistrationPage import RegistrationPage
from Pages.SportsPage import SportsPage


class MainPage(BasePage):
    SPORTS_BUTTON = (By.XPATH, '//a[@href="/sport"]')
    LV_FLAG = '//img[@src="https://content.optibet.lv/_ui/flags/lv.svg"]'
    COOKIES_BTN = '//span[text()="Pieņemt"]'
    REGISTRATION = (By.XPATH, './/div[@id="topBar"]//button[@data-role="signupHeaderButton"]')
    LOGIN_BUTTON = (By.XPATH, '//div[@id="topBar"]//button[@data-role="loginHeaderButton"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def select_lv_flag(self):
        if self.check_exists_by_xpath(self.LV_FLAG):
            self.driver.find_element(By.XPATH, self.LV_FLAG).click()

    def accept_cookies(self):
        if self.check_exists_by_xpath(self.COOKIES_BTN):
            self.driver.find_element(By.XPATH, self.COOKIES_BTN).click()

    def navigate_sports(self):
        self.do_click(self.SPORTS_BUTTON)
        return SportsPage(self.driver)

    def navigate_registration(self):
        self.do_click(self.REGISTRATION)
        return RegistrationPage(self.driver)

    def navigate_login(self):
        self.do_clickable_click(by_locator=self.LOGIN_BUTTON)
        return CasinoPage(self.driver)
