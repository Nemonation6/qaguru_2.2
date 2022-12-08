import os

from selene.support.shared import browser
from selene import have, command

from tests.model import app
from tests.model.utilities.path import path_to
from tests.users import danil


state = browser.element('#state')


def test_student_registration_form():

    app.practise_form_page.given_opened_text_box_page()

    #WHEN

    app.practise_form_page.verify_title("ToolsQA")

    app.practise_form_page.set_full_name(danil.student.name, danil.student.last_name)

    app.practise_form_page.set_email(danil.student.email)

    app.practise_form_page.set_gender(danil.student.gender)

    app.practise_form_page.set_phone_number(danil.student.user_number)

    browser.execute_script("window.scrollTo(0, 100)")

    app.practise_form_page.set_birth_date(danil.student.birth_month,
                                          danil.student.birth_year, danil.student.birth_day)

    app.practise_form_page.add_subjects(danil.student.subjects)

    app.practise_form_page.add_hobbies(danil.student.hobbies)

    browser.execute_script("window.scrollTo(0, 200)")

    app.practise_form_page.upload_picture(danil.student.picture_file)

    app.practise_form_page.set_current_adress(danil.student.current_address)

    browser.execute_script("window.scrollTo(0, 400)")

    app.practise_form_page.set_state(danil.student.state)

    app.practise_form_page.set_city(danil.student.city)

    app.practise_form_page.submit_form()

    #THEN

    subjects = app.practise_form_page.get_subjects_list(danil.student.subjects)

    hobbies = app.practise_form_page.get_hobby_list(danil.student.hobbies)

    app.practise_form_page.should_have_submitted(
        [
            ('Student Name', f'{danil.student.name} {danil.student.last_name}'),
            ('Student Email', danil.student.email),
            ('Gender', danil.student.gender.value),
            ('Mobile', danil.student.user_number),
            ('Date of Birth', f'{danil.student.birth_day} {danil.student.birth_month},{danil.student.birth_year}'),
            ('Subjects', subjects),
            ('Hobbies', hobbies),
            ('Picture', danil.student.picture_file),
            ('Address', danil.student.current_address),
            ('State and City', f'{danil.student.state} {danil.student.city}')
        ],
    )

