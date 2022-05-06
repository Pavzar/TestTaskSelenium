import random
import time

import js2py
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from textwrap import wrap
from nickname_generator import generate
from Pages.BasePage import BasePage
from Pages.HomePage import HomePage


class RegistrationPage(BasePage):
    COPY_FAKE_EMAIL_BUTTON = (By.XPATH, './/button[@id="copy-button"]')
    EMAIL_FIELD = (By.XPATH, './/form//input[@name="email"]')
    PASSWORD_FIELD = (By.XPATH, './/input[@name="password"]')
    TOS_CHECKBOX = (By.XPATH, './/input[@name="tnc"]//following-sibling::span')
    PROMOTIONS_CHECKBOX = (By.XPATH, './/input[@name="promotions"]//following-sibling::span')
    SUBMIT_BTN = (By.XPATH, './/button[@type="submit"]')

    PIN = (By.XPATH, './/table[@class="email-container"]//strong')
    PIN_FIELD = (By.XPATH, '//input[@name="code"]')
    IFRAME_ID = (By.ID, 'emailFrame')
    IFRAME_PERSONAL_ID = (By.ID, 'result')
    PERSONAL_ID_FIELD = (By.XPATH, './/input[@name="personalId"]')
    GENERATED_PERSONAL_ID = (By.XPATH, './/button//following-sibling::div')
    CALCULATE_BUTTON = (By.XPATH, '//button[text()="calculate"]')
    PHONE_FIELD = (By.XPATH, '//input[@name="phoneNumber"]')
    FIRSTNAME_FIELD = (By.XPATH, '//input[@name="firstName"]')
    LASTNAME_FIELD = (By.XPATH, '//input[@name="lastName"]')

    DAY_DROPDOWN = (By.XPATH, './/div[@data-role="additionalDobDay"]')
    MONTH_DROPDOWN = (By.XPATH, './/div[@data-role="additionalDobMonth"]')
    YEAR_DROPDOWN = (By.XPATH, './/div[@data-role="additionalDobYear"]')

    OTHER_BUTTON = (By.XPATH, '//div[@data-role="Other"]')
    FEMALE_BUTTON = (By.XPATH, '//div[@data-role="Female"]')
    MALE_BUTTON = (By.XPATH, '//div[@data-role="Male"]')

    SUBMIT_BTN_ADDITIONAL = (By.XPATH, '//button[@data-role="additionalSubmit"]')

    EMAIL_COPY = (By.XPATH, '//span[@id="cxtEmail"]')

    def __init__(self, driver):
        super().__init__(driver)

    def set_sex(self):
        n = random.randint(1, 3)
        if n == 1:
            self.do_click(by_locator=self.MALE_BUTTON)
        elif n == 2:
            self.do_click(by_locator=self.FEMALE_BUTTON)
        else:
            self.do_click(by_locator=self.OTHER_BUTTON)

    def set_phone(self):
        phone_number = self.get_phone_number()
        self.do_send_keys(by_locator=self.PHONE_FIELD, text=phone_number)

    def paste_text(self):
        ActionChains(self.driver).key_down(Keys.CONTROL).perform()
        ActionChains(self.driver).send_keys("v").perform()
        ActionChains(self.driver).reset_actions()

    def set_full_name(self):
        first_name = generate()
        last_name = generate()
        self.do_send_keys(by_locator=self.FIRSTNAME_FIELD, text=first_name)
        self.do_send_keys(by_locator=self.LASTNAME_FIELD, text=last_name)

    def switch_to_iframe_email(self):
        self.switch_to_iframe(self.IFRAME_ID)

    def switch_to_iframe_id(self):
        self.switch_to_iframe(self.IFRAME_PERSONAL_ID)

    def generate_personal_id(self):
        js = """
        function getRandomPersonalId() {
          var currentDate = new Date();

          var maxAgeInMilis = 45 * 365 * 24 * 60 * 60 * 1000;
          var minAgeInMilis = 21 * 365 * 24 * 60 * 60 * 1000;
          var randomMilis = Math.floor((Math.random() * maxAgeInMilis) + minAgeInMilis);

          var time = currentDate.setTime(currentDate.getTime() - randomMilis);
          var date = new Date(time);

          var day = padWithLeadingZeros(date.getDate());
          var month = padWithLeadingZeros(date.getMonth() + 1);
          var shortYear = date.getFullYear().toString().substring(2);
          var firstPart = day + "" + month + "" + shortYear;

          var checkDigit = "00";
          while (checkDigit.toString().length === 2) {
            pk = firstPart + getSecondPart();
            checkDigit = getCheckDigit(pk);
          };

          pk = pk + checkDigit;
          pk = pk.substring(0, 6) + "-" + pk.substring(6);

          return pk;
        };

        function padWithLeadingZeros(value) {
          value = value.toString();
          return value.length === 1 ? "0".concat(value) : value;
        };

        function getCheckDigit(pk) {
          var factor = [1, 6, 3, 7, 9, 10, 5, 8, 4, 2];

          pk = pk.split("").map(function(i) { return parseInt(i)});

          var reduce = pk.reduce(function(prev, cur, i) { return cur * factor[i] + prev } );

          return (1101 - reduce) % 11;
        };

        function getSecondPart() {
          return "1" + Math.floor((Math.random() * 899) + 100);
        };

        getRandomPersonalId()
        """
        personal_code = js2py.eval_js(js)
        time.sleep(0.2)
        self.do_send_keys(self.PERSONAL_ID_FIELD, personal_code)

        return personal_code

    def set_date_of_birth(self):
        personal_id = self.generate_personal_id()
        self.do_click(by_locator=self.DAY_DROPDOWN)
        split_id = personal_id.split("-")
        split_date_of_birth = wrap(split_id[0], 2)

        if int(split_date_of_birth[0]) < 10:
            format_xpath = (By.XPATH, './/div[@data-role="additionalDobDay{day}"]'.format(
                day=int(split_date_of_birth[0].lstrip('0')) - 1))
            self.do_click(format_xpath)
        else:
            format_xpath = (By.XPATH, './/div[@data-role="additionalDobDay{day}"]'.format(day=int(split_date_of_birth[0]) - 1))
            self.do_click(format_xpath)

        self.do_click(by_locator=self.MONTH_DROPDOWN)

        if int(split_date_of_birth[1]) < 10:
            format_xpath = (By.XPATH, './/div[@data-role="additionalDobMonth{month}"]'.format(
                month=int(split_date_of_birth[1].lstrip('0')) - 1))
            self.do_click(format_xpath)
        else:
            format_xpath = (
            By.XPATH, './/div[@data-role="additionalDobMonth{month}"]'.format(month=int(split_date_of_birth[1]) - 1))
            self.do_click(format_xpath)

        self.do_click(by_locator=self.YEAR_DROPDOWN)

        if int(split_date_of_birth[2]) < 5:
            format_xpath = (By.XPATH, './/div[@data-value="{year}"]"]'.format(
                year=('20' + split_date_of_birth[2])))
            self.do_click(format_xpath)
        elif 5 <= int(split_date_of_birth[2]) < 10:
            format_xpath = (By.XPATH, './/div[@data-value="{year}"]"]'.format(
                year=('19' + split_date_of_birth[2])))
            self.do_click(format_xpath)
        else:
            format_xpath = (By.XPATH, './/div[@data-value="{year}"]'.format(year=('19' + split_date_of_birth[2])))
            self.do_click(format_xpath)

    def get_fake_email(self):
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get("http://www.fakemailgenerator.com")
        self.do_clickable_click(self.COPY_FAKE_EMAIL_BUTTON)
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.do_clickable_click(self.EMAIL_FIELD)
        self.paste_text()
        time.sleep(0.3)
        self.do_clickable_click(by_locator=self.PASSWORD_FIELD)
        self.do_send_keys(by_locator=self.PASSWORD_FIELD, text='Test123')
        self.do_clickable_click(self.TOS_CHECKBOX)
        self.do_clickable_click(self.PROMOTIONS_CHECKBOX)
        self.do_clickable_click(self.SUBMIT_BTN)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.switch_to_iframe_email()
        pin_copy = self.get_text(self.PIN)
        self.switch_from_iframe()
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.do_send_keys(self.PIN_FIELD, pin_copy)

    def get_phone_number(self):
        first = str(random.randint(100, 999))
        second = str(random.randint(1, 888)).zfill(3)
        last = (str(random.randint(1, 9998)).zfill(4))

        while last in ['1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888']:
            last = (str(random.randint(1, 9998)).zfill(4))

        return '{}{}{}'.format(first, second, last)

    def click_additional_submit(self):
        time.sleep(0.2)
        self.do_clickable_click(by_locator=self.SUBMIT_BTN_ADDITIONAL)
        return HomePage(self.driver)

