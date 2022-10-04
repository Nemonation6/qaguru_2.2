import pytest
from selene.support.shared import browser
from selene import be, have


@pytest.fixture()
def open_page():
    browser.open('https://www.google.com/ncr')


def test_1(open_page):
    browser.element('[name="q"]').should(be.blank).type('selene python').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser'
                                                      ' tests in Python'))
