from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.service import Service
from selene import browser, config
import pytest


@pytest.fixture(scope='function', autouse=True)
def driver_setup(request):

    if request.config.getoption('--browser') == 'chrome':
        option = ChromeOptions()

        if request.config.getoption('--headless'):
            option.add_argument('--headless')

        # Если нужно передать локальный путь до драйвера используем Service() и передаем в него путь до драйвера.
        # service = Service(r'/home/asmo/Downloads/chromedriver-linux64/chromedriver')
        service = None
        driver = Chrome(options=option, service=service)

    else:
        raise ValueError('Wrong browser type')

    driver.maximize_window()
    browser.set_driver(driver)
    config.base_url = 'https://demoqa.com'


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome', help='Set a browser to launch')
    parser.addoption('--headless', action='store', default=False, help='Browser headless mode')
