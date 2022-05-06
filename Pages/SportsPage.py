import time

from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from Pages.LoginPage import LoginPage


class SportsPage(BasePage):
    ODD_BTN = (By.XPATH, '//div[@class="odd"]')
    ICON = (By.XPATH, '//div[@class="empty-stub"]')
    BET_BTN = (By.XPATH, '//div[@class="total"]//following-sibling::button')
    IFRAME_ID = (By.ID, 'iFrameResizer0')

    def switch_to_iframe_bet(self):
        self.switch_to_iframe(self.IFRAME_ID)

    def select_odd(self):
        if self.is_visible(by_locator=self.ICON):
            time.sleep(0.1)
            self.do_clickable_click(by_locator=self.ODD_BTN)

    def place_bet(self):
        self.do_clickable_click(by_locator=self.BET_BTN)
        return LoginPage(self.driver)
