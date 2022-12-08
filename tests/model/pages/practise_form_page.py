from typing import Tuple

from selene import have, command, by
from selene.support.shared import browser
from .. import controls

from tests.users.danil import Subject, Hobby
from ..controls import modal
from ..utilities import path


def given_opened_text_box_page():
    browser.open("/automation-practice-form")
    ads = browser.all('[id^=google_ads_][id$=container__]')
    ads.wait.until(have.size_greater_than_or_equal(3))
    ads.perform(command.js.remove)


def verify_title(title):
    browser.should(have.title(title))


def set_full_name(first_name, last_name):
    browser.element("#firstName").type(first_name)
    browser.element("#lastName").type(last_name)


def set_email(email):
    browser.element("#userEmail").type(email)


def set_gender(gender):
    browser.all('[for^=gender-radio]').by(have.exact_text(gender.value)).first.click()


def set_phone_number(phone_number):
    browser.element("#userNumber").type(phone_number)


def set_birth_date(birth_month, birth_year, birth_day):
    controls.datepicker.select_birth_date(birth_month, birth_year, birth_day)


def add_subjects(values: Tuple[Subject]):
    for subject in values:
        browser.element('#subjectsInput').type(subject.value).press_enter()


def get_subjects_list(values: Tuple[Subject]):
    subjects = ''

    for subject in values:
        subjects = subjects + str(subject.value) + ', '

    subjects = subjects.rstrip(', ')

    return subjects


def add_hobbies(values: Tuple[Hobby]):
    for hobby in values:
        hobby_xpath = "//label[contains(.,'" + str(hobby.value) + "')]"
        browser.element(by.xpath(hobby_xpath)).click()


def get_hobby_list(values: Tuple[Subject]):
    hobbies = ''

    for hobby in values:
        hobbies = hobbies + str(hobby.value) + ', '

    hobbies = hobbies.rstrip(', ')

    return hobbies


def upload_picture(picture_file: str):
    browser.element('#uploadPicture').send_keys(path.path_to(picture_file))


def set_current_adress(current_adress):
    browser.element('#currentAddress').type(current_adress)


state = browser.element('#state')
city = browser.element('#city')


def set_state(value: str):
    controls.dropdown.select(state, value)


def set_city(value: str):
    controls.dropdown.select(city, value)


def submit_form():
    browser.element('#submit').perform(command.js.click)


def should_have_submitted(data):
    rows = modal.dialog.all('tbody tr')
    for row, value in data:
        rows.element_by(have.text(row)).all('td')[1].should(have.exact_text(value))


