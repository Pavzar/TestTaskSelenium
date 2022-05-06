import pytest
from selenium import webdriver
from selenium_stealth import stealth
from Config.config import TestData


@pytest.fixture(autouse=True)
def init_driver(request):

    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    web_driver = webdriver.Chrome(options=options, executable_path=TestData.CHROME_EXECUTABLE_PATH)
    request.cls.driver = web_driver

    # Selenium Stealth settings
    stealth(web_driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            )
    yield
    web_driver.quit()
