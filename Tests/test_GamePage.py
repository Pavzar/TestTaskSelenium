from Config.config import TestData
from Pages.GamePage import GamePage
from Pages.MainPage import MainPage
from Tests.test_base import BaseTest


class TestGame(BaseTest):
    def navigate_to_game(self):
        self.mainPage = MainPage(self.driver)
        self.mainPage.select_lv_flag()
        self.mainPage.accept_cookies()
        casino_page = self.mainPage.navigate_login()
        casino_page.login()
        casino_page.navigate_casino_page()
        casino_page.click_game()
        return GamePage(self.driver)

    def test_game_restricted_title_lv(self):
        game_page = self.navigate_to_game()
        restricted_title_visible = game_page.is_restricted_title_visible()
        restricted_title_text = game_page.get_restricted_title_text()

        assert restricted_title_visible
        assert restricted_title_text == TestData.RESTRICTED_LV

    def test_game_restricted_title_eng(self):
        game_page = self.navigate_to_game()
        game_page.choose_eng_language()
        restricted_title_visible = game_page.is_restricted_title_visible()
        restricted_title_text = game_page.get_restricted_title_text()

        assert restricted_title_visible
        assert restricted_title_text == TestData.RESTRICTED_ENG

    def test_game_restricted_title_ru(self):
        game_page = self.navigate_to_game()
        game_page.choose_ru_language()
        restricted_title_visible = game_page.is_restricted_title_visible()
        restricted_title_text = game_page.get_restricted_title_text()

        assert restricted_title_visible
        assert restricted_title_text == TestData.RESTRICTED_RU

    def test_game_restricted_content_lv(self):
        game_page = self.navigate_to_game()
        restricted_content_visible = game_page.is_restricted_content_visible()
        restricted_content_text = game_page.get_restricted_content_text()

        assert restricted_content_visible
        assert restricted_content_text == TestData.CONTENT_LV

    def test_game_restricted_content_eng(self):
        game_page = self.navigate_to_game()
        game_page.choose_eng_language()
        restricted_content_visible = game_page.is_restricted_content_visible()
        restricted_content_text = game_page.get_restricted_content_text()

        assert restricted_content_visible
        assert restricted_content_text == TestData.CONTENT_ENG

    def test_game_restricted_content_ru(self):
        game_page = self.navigate_to_game()
        game_page.choose_ru_language()
        restricted_content_visible = game_page.is_restricted_content_visible()
        restricted_content_text = game_page.get_restricted_content_text()

        assert restricted_content_visible
        assert restricted_content_text == TestData.CONTENT_RU



