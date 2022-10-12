import os

import pytest
from selene.support.shared import browser
from selene import have, command


def given_opened_text_box_page():
    browser.open("/automation-practice-form")
    ads = browser.all('[id^=google_ads_][id$=container__]')
    if ads.wait.until(have.size_greater_than_or_equal(3)):
        ads.perform(command.js.remove)


def test_student_registration_form():
    given_opened_text_box_page()
    browser.should(have.title("ToolsQA"))
    browser.element("#firstName").type("Dan")
    browser.element("#lastName").type("Roz")
    browser.element("#userEmail").type("DR@olol.com")
    browser.element("[for=gender-radio-1]").click()
    browser.element("#userNumber").type("1234567890")
    browser.execute_script("window.scrollTo(0, 100)")
    browser.element('#dateOfBirthInput').perform(command.js.set_value('26 May 1999'))
    browser.element('#subjectsInput').click().type("ma").press_enter()
    browser.execute_script("window.scrollTo(0, 200)")
    hobby_checkbox_1.click()
    hobby_checkbox_2.click()
    hobby_checkbox_3.click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('tests/kitten.jpg'))
    browser.element('#currentAddress').type('Tbilisi lol str 56 b 22 apt')
    browser.execute_script("window.scrollTo(0, 400)")
    state.type("har").press_enter()
    city.type("a").press_enter()


hobby_checkbox_1 = browser.element('[for="hobbies-checkbox-1"]')
hobby_checkbox_2 = browser.element('[for="hobbies-checkbox-2"]')
hobby_checkbox_3 = browser.element('[for="hobbies-checkbox-3"]')
state = browser.element('#react-select-3-input')
city = browser.element('#react-select-4-input')