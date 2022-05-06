from Config.config import TestData
from Pages.MainPage import MainPage
from Tests.test_base import BaseTest


class TestRegistration(BaseTest):

    # Sometimes website won't let me make another account
    # https://miro.medium.com/max/1000/1*vP1drWY1myDhV99P9YHhGg.png

    def switch_to_registration_page_and_register(self):
        self.mainPage = MainPage(self.driver)
        self.mainPage.select_lv_flag()
        self.mainPage.accept_cookies()
        registration_page = self.mainPage.navigate_registration()
        registration_page.get_fake_email()
        registration_page.set_phone()
        registration_page.set_full_name()
        registration_page.set_date_of_birth()
        registration_page.set_sex()
        home_page = registration_page.click_additional_submit()
        return home_page

    # mandatory limit pop-up appears as first
    def test_mandatory_limit_popup_visible(self):
        home_page = self.switch_to_registration_page_and_register()
        mandatory_pop_up = home_page.is_mandatory_pop_up_visible()

        assert mandatory_pop_up

    # check all links (button) on the welcome pop-up
    def test_mandatory_limit_set_success_visible(self):
        home_page = self.switch_to_registration_page_and_register()
        home_page.click_mandatory_submit()
        limit_set_success_visible = home_page.is_limit_set_success_visible()

        assert limit_set_success_visible

    def test_welcome_pop_up_visible(self):
        home_page = self.switch_to_registration_page_and_register()
        home_page.click_mandatory_submit()
        home_page.click_close_limit_success()

        welcome_pop_up_visible = home_page.is_welcome_pop_up_visible()

        assert welcome_pop_up_visible

    def test_limits_button_welcome_pop_up_visible(self):
        home_page = self.switch_to_registration_page_and_register()
        home_page.click_mandatory_submit()
        home_page.click_close_limit_success()
        limits_button_visible = home_page.is_welcome_pop_up_limits_button_visible()

        assert limits_button_visible

    def test_deposit_button_welcome_pop_up_visible(self):
        home_page = self.switch_to_registration_page_and_register()
        home_page.click_mandatory_submit()
        home_page.click_close_limit_success()
        deposit_button_visible = home_page.is_welcome_pop_up_deposit_button_visible()

        assert deposit_button_visible

    def test_casino_button_welcome_pop_up_visible(self):
        home_page = self.switch_to_registration_page_and_register()
        home_page.click_mandatory_submit()
        home_page.click_close_limit_success()
        casino_button_visible = home_page.is_welcome_pop_up_casino_button_visible()

        assert casino_button_visible

    def test_sports_button_welcome_pop_up_visible(self):
        home_page = self.switch_to_registration_page_and_register()
        home_page.click_mandatory_submit()
        home_page.click_close_limit_success()
        sports_button_visible = home_page.is_welcome_pop_up_sports_button_visible()

        assert sports_button_visible

    def test_livecasino_button_welcome_pop_up_visible(self):
        home_page = self.switch_to_registration_page_and_register()
        home_page.click_mandatory_submit()
        home_page.click_close_limit_success()
        livecasino_button_visible = home_page.is_welcome_pop_up_livecasino_button_visible()

        assert livecasino_button_visible

    def test_limits_button_welcome_pop_up_link(self):
        home_page = self.switch_to_registration_page_and_register()
        home_page.click_mandatory_submit()
        home_page.click_close_limit_success()
        home_page.click_limits_button_welcome_pop_up()
        current_url = home_page.get_current_url()
        limits_link_opened = home_page.is_limits_link_opened()

        assert current_url == TestData.LIMITS_URL
        assert limits_link_opened

    def test_deposit_button_welcome_pop_up_link(self):
        home_page = self.switch_to_registration_page_and_register()
        home_page.click_mandatory_submit()
        home_page.click_close_limit_success()
        home_page.click_deposit_button_welcome_pop_up()
        current_url = home_page.get_current_url()
        deposit_link_opened = home_page.is_deposit_link_opened()

        assert current_url == TestData.DEPOSIT_URL
        assert deposit_link_opened

    def test_casino_button_welcome_pop_up_link(self):
        home_page = self.switch_to_registration_page_and_register()
        home_page.click_mandatory_submit()
        home_page.click_close_limit_success()
        home_page.click_casino_button_welcome_pop_up()
        current_url = home_page.get_current_url()
        casino_link_opened = home_page.is_casino_link_opened()

        assert current_url == TestData.CASINO_URL
        assert casino_link_opened

    def test_sports_button_welcome_pop_up_link(self):
        home_page = self.switch_to_registration_page_and_register()
        home_page.click_mandatory_submit()
        home_page.click_close_limit_success()
        home_page.click_sports_button_welcome_pop_up()
        current_url = home_page.get_current_url()
        sports_link_opened = home_page.is_sports_link_opened()

        assert current_url == TestData.SPORTS_URL
        assert sports_link_opened

    def test_livecasino_button_welcome_pop_up_link(self):
        home_page = self.switch_to_registration_page_and_register()
        home_page.click_mandatory_submit()
        home_page.click_close_limit_success()
        home_page.click_livecasino_button_welcome_pop_up()
        current_url = home_page.get_current_url()
        livecasino_link_opened = home_page.is_livecasino_link_opened()

        assert current_url == TestData.LIVECASINO_URL
        assert livecasino_link_opened
