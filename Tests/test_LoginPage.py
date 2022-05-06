from Config.config import TestData
from Pages.MainPage import MainPage
from Tests.test_base import BaseTest


class TestLogin(BaseTest):

    def switch_to_sports_page(self):
        self.mainPage = MainPage(self.driver)
        self.mainPage.select_lv_flag()
        self.mainPage.accept_cookies()
        sports_page = self.mainPage.navigate_sports()
        sports_page.switch_to_iframe_bet()
        sports_page.select_odd()
        login_page = sports_page.place_bet()
        sports_page.switch_from_iframe()
        return login_page

    def test_login_popup(self):
        login_page = self.switch_to_sports_page()
        login_popup_appeared = login_page.is_login_popup_appeared()
        current_url = login_page.get_current_url()

        assert TestData.LOGIN_URL == current_url
        assert login_popup_appeared

    def test_login_field(self):
        login_page = self.switch_to_sports_page()
        login_field_visible = login_page.is_login_field_visible()
        login_label_text = login_page.get_login_field_label_text()

        assert login_field_visible
        assert login_label_text == TestData.LOGIN_LABEL

    def test_password_field(self):
        login_page = self.switch_to_sports_page()
        password_field_visible = login_page.is_password_field_visible()
        password_label_text = login_page.get_password_field_label_text()

        assert password_field_visible
        assert password_label_text == TestData.PASSWORD_LABEL

    def test_hide_password_icon_visible(self):
        login_page = self.switch_to_sports_page()
        hide_password_icon_visible = login_page.is_hide_password_visible()

        assert hide_password_icon_visible

    def test_hide_password_func(self):
        login_page = self.switch_to_sports_page()
        hide_password_func_setting = login_page.is_hide_password_attribute_changed()

        assert hide_password_func_setting

    def test_id_field(self):
        login_page = self.switch_to_sports_page()
        login_page.click_smartid()
        id_field_visible = login_page.is_id_field_visible()
        id_field_label_text = login_page.get_id_label_text()

        assert id_field_visible
        assert id_field_label_text == TestData.ID_LABEL

    def test_id_field_symbols_error_message(self):
        login_page = self.switch_to_sports_page()
        login_page.click_smartid()
        login_page.type_symbols_id_field()
        id_field_symbols_error_message = login_page.get_id_field_error_message()

        assert id_field_symbols_error_message == TestData.ID_FIELD_SYMBOLS_ERROR_MESSAGE

    def test_id_field_empty_error_message(self):
        login_page = self.switch_to_sports_page()
        login_page.click_smartid()
        login_page.click_smartid_submit()
        id_field_error_message = login_page.get_id_field_error_message()

        assert id_field_error_message == TestData.ID_FIELD_ERROR_MESSAGE

    def test_id_field_false_error_message(self):
        login_page = self.switch_to_sports_page()
        login_page.click_smartid()
        login_page.type_false_id()
        login_page.click_smartid_submit()
        id_field_false_error_message = login_page.get_id_field_error_message()

        assert id_field_false_error_message == TestData.ID_FIELD_FALSE_ERROR_MESSAGE

    def test_signup_link(self):
        login_page = self.switch_to_sports_page()
        signup_link_visible = login_page.is_signup_link_visible()
        signup_link_clickable = login_page.is_signup_link_clickable()

        assert signup_link_clickable
        assert signup_link_visible

    def test_forgot_password(self):
        login_page = self.switch_to_sports_page()
        forgot_password_link_visible = login_page.is_forgot_password_visible()
        forgot_password_link_clickable = login_page.is_forgot_password_clickable()

        assert forgot_password_link_visible
        assert forgot_password_link_clickable

    def test_submit_btn(self):
        login_page = self.switch_to_sports_page()
        submit_button_visible = login_page.is_submit_button_visible()
        submit_button_clickable = login_page.is_submit_button_clickable()
        submit_button_text = login_page.get_submit_button_text()

        assert submit_button_visible
        assert submit_button_clickable
        assert submit_button_text == TestData.LOGIN_SUBMIT_BUTTON_TEXT

    def test_form_validation_empty(self):
        login_page = self.switch_to_sports_page()
        login_page.click_submit()
        login_error_message = login_page.get_login_error_message()
        password_error_message = login_page.get_password_error_message()

        assert login_error_message == TestData.LOGIN_ERROR_MESSAGE
        assert password_error_message == TestData.PASSWORD_ERROR_MESSAGE

    def test_form_validation_short_login(self):
        login_page = self.switch_to_sports_page()
        login_page.type_short_login()
        login_short_error_message = login_page.get_login_error_message()

        assert login_short_error_message == TestData.LOGIN_SHORT_ERROR_MESSAGE

    def test_form_validation_long_login(self):
        login_page = self.switch_to_sports_page()
        login_page.type_long_login()
        login_long_error_message = login_page.get_login_error_message()

        assert login_long_error_message == TestData.LOGIN_LONG_ERROR_MESSAGE

    def test_form_validation_symbols_login(self):
        login_page = self.switch_to_sports_page()
        login_page.type_symbols_login()
        login_symbols_error_message = login_page.get_login_error_message()

        assert login_symbols_error_message == TestData.LOGIN_SYMBOLS_ERROR_MESSAGE

    def test_form_false_login(self):
        login_page = self.switch_to_sports_page()
        login_page.type_false_login()
        login_false_error_message = login_page.get_password_error_message()

        assert login_false_error_message == TestData.FALSE_LOGIN
