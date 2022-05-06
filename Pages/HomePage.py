import time

from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class HomePage(BasePage):
    MANDATORY_POP_UP = (By.XPATH, '//div[@class="dialog-title___ga1UR--scss" and @data-role="dialogTitle"]')
    MANDATORY_POP_UP_SUBMIT_BTN = (By.XPATH, '//form//button[@type="submit"]')

    LIMIT_SET_SUCCESS_POPUP = (By.XPATH, '//div[@data-role="successDialogTitle"]')
    SUCCESS_CLOSE_BUTTON = (By.XPATH, '//button[@data-role="successDialogCloseButton"]')
    WELCOME_POP_UP = (By.XPATH, '//div[@data-role="textWelcomePopUp"]')

    LIMITS_WELCOME_BUTTON = (By.XPATH, '//button[@data-role="limitsWelcomePopUp"]')
    DEPOSIT_WELCOME_BUTTON = (By.XPATH, '//button[@data-role="depositWelcomePopUp"]')
    CASINO_WELCOME_BUTTON = (By.XPATH, '//button[@data-role="casinoWelcomePopUp"]')
    SPORTS_WELCOME_BUTTON = (By.XPATH, '//button[@data-role="sportsbookWelcomePopUp"]')
    LIVECASINO_WELCOME_BUTTON = (By.XPATH, '//button[@data-role="livecasinoWelcomePopUp"]')

    AVAILABLE_CAMPAIGNS_WELCOME_LINK = (By.XPATH, '//a[@data-role="availableCampaignsWelcomePopUp"]')

    ADD_LIMITS_BUTTON = (By.XPATH, '//button[@data-role="addLimitsButton"]')
    DEPOSIT_PROVIDERS = (By.XPATH, '//button[@data-role="deposit-paymentiq_card-Button"]')
    CASINO_FILTER_LINK = (By.XPATH, '//div[@data-role="categoryTitle"]//following::a[@href="/casino/optibet-favourites"]')
    SPORTS_IFRAME = (By.XPATH, '//iframe[@id="iFrameResizer0"]')
    LIVECASINO_FILTER_LINK = (By.XPATH, '//div[@data-role="categoryTitle"]//following::a[@href="/live-casino/popular-live"]')
    BONUS_TOGGLE_MENU = (By.XPATH, '//div[@data-role="toggleMenuMyBonus"]')

    def __init__(self, driver):
        self.driver = driver

    def is_mandatory_pop_up_visible(self):
        return self.is_visible(by_locator=self.MANDATORY_POP_UP)

    def is_welcome_pop_up_visible(self):
        return self.is_visible(by_locator=self.WELCOME_POP_UP)

    def is_limit_set_success_visible(self):
        return self.is_visible(by_locator=self.LIMIT_SET_SUCCESS_POPUP)

    def is_welcome_pop_up_limits_button_visible(self):
        return self.is_visible(by_locator=self.LIMITS_WELCOME_BUTTON)

    def is_welcome_pop_up_deposit_button_visible(self):
        return self.is_visible(by_locator=self.DEPOSIT_WELCOME_BUTTON)

    def is_welcome_pop_up_casino_button_visible(self):
        return self.is_visible(by_locator=self.CASINO_WELCOME_BUTTON)

    def is_welcome_pop_up_sports_button_visible(self):
        return self.is_visible(by_locator=self.SPORTS_WELCOME_BUTTON)

    def is_welcome_pop_up_livecasino_button_visible(self):
        return self.is_visible(by_locator=self.LIVECASINO_WELCOME_BUTTON)

    def is_limits_link_opened(self):
        return self.is_visible(by_locator=self.ADD_LIMITS_BUTTON)

    def is_deposit_link_opened(self):
        return self.is_visible(by_locator=self.DEPOSIT_PROVIDERS)

    def is_casino_link_opened(self):
        return self.is_visible(by_locator=self.CASINO_FILTER_LINK)

    def is_sports_link_opened(self):
        return self.is_visible(by_locator=self.SPORTS_IFRAME)

    def is_livecasino_link_opened(self):
        return self.is_visible(by_locator=self.LIVECASINO_FILTER_LINK)

    def click_mandatory_submit(self):
        time.sleep(0.1)
        self.do_clickable_click(by_locator=self.MANDATORY_POP_UP_SUBMIT_BTN)

    def click_close_limit_success(self):
        time.sleep(0.1)
        self.do_clickable_click(by_locator=self.SUCCESS_CLOSE_BUTTON)

    def click_limits_button_welcome_pop_up(self):
        time.sleep(0.1)
        self.do_clickable_click(by_locator=self.LIMITS_WELCOME_BUTTON)

    def click_deposit_button_welcome_pop_up(self):
        time.sleep(0.1)
        self.do_clickable_click(by_locator=self.DEPOSIT_WELCOME_BUTTON)

    def click_casino_button_welcome_pop_up(self):
        time.sleep(0.1)
        self.do_clickable_click(by_locator=self.CASINO_WELCOME_BUTTON)

    def click_sports_button_welcome_pop_up(self):
        time.sleep(0.1)
        self.do_clickable_click(by_locator=self.SPORTS_WELCOME_BUTTON)

    def click_livecasino_button_welcome_pop_up(self):
        time.sleep(0.1)
        self.do_clickable_click(by_locator=self.LIVECASINO_WELCOME_BUTTON)

