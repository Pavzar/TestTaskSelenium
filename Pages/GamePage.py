from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class GamePage(BasePage):
    RESTRICTED_TITLE = (By.XPATH, '//h2[@data-role="restrictedTitle"]')
    RESTRICTED_CONTENT = (By.XPATH, '//div[@data-role="restrictedContent"]')
    LANGUAGE_BUTTON = (By.XPATH, '//div[@class="container___IU_AD--scss hiddenDesktop___bYqiZ--scss"]')
    SELECT_ENG = (By.XPATH, '//div[@class="container___IU_AD--scss hiddenDesktop___bYqiZ--scss"]//a[@data-id="langMenuItem-en"]')
    SELECT_RU = (By.XPATH, '//div[@class="container___IU_AD--scss hiddenDesktop___bYqiZ--scss"]//a[@data-id="langMenuItem-ru"]')

    def __init__(self, driver):
        super().__init__(driver)

    def is_restricted_title_visible(self):
        return self.is_visible(by_locator=self.RESTRICTED_TITLE)

    def is_restricted_content_visible(self):
        return self.is_visible(by_locator=self.RESTRICTED_CONTENT)

    def get_restricted_title_text(self):
        return self.get_text(xpath=self.RESTRICTED_TITLE)

    def get_restricted_content_text(self):
        return self.get_text(xpath=self.RESTRICTED_CONTENT)

    def choose_eng_language(self):
        self.do_clickable_click(by_locator=self.LANGUAGE_BUTTON)
        self.do_clickable_click(by_locator=self.SELECT_ENG)

    def choose_ru_language(self):
        self.do_clickable_click(by_locator=self.LANGUAGE_BUTTON)
        self.do_clickable_click(by_locator=self.SELECT_RU)
