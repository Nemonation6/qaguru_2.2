import pytest
from selene.support.shared import browser


@pytest.fixture(scope='function', autouse=True)
def open_page():
    browser.config.base_url = "https://demoqa.com"
