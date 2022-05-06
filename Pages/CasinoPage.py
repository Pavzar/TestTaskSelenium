from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class CasinoPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    username = 'Laut1958@superrito.com'
    password = 'Test123'

    LOGIN_FIELD = (By.XPATH, './/form//child::input[@name="email"]')
    PASSWORD_FIELD = (By.XPATH, './/form//input[@name="password"]')
    SUBMIT_BTN = (By.XPATH, './/form//button[@type="submit"]')
    CASINO_WELCOME_BUTTON = (By.XPATH, '//button[@data-role="casinoWelcomePopUp"]')
    GAME_BUTTON = (By.XPATH, '//h2[text()="Optibet iesaka"]//following::div[@data-role="gameThumb"][1]')

    def login(self):
        self.do_send_keys(by_locator=self.LOGIN_FIELD, text=self.username)
        self.do_send_keys(by_locator=self.PASSWORD_FIELD, text=self.password)
        self.do_clickable_click(by_locator=self.SUBMIT_BTN)

    def navigate_casino_page(self):
        self.do_clickable_click(by_locator=self.CASINO_WELCOME_BUTTON)

    def click_game(self):
        self.do_clickable_click(by_locator=self.GAME_BUTTON)








