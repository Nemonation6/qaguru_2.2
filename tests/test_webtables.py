from selene import command, have
from selene.support.shared import browser


def given_opened_webtables_page():
    browser.open("/webtables")
    ads = browser.all('[id^=google_ads_][id$=container__]')
    ads.wait.until(have.size_greater_than_or_equal(3))
    ads.perform(command.js.remove)


def test_add_delete_edit():
    given_opened_webtables_page()
    browser.should(have.title('ToolsQA'))
    browser.element("#addNewRecordButton").click()
    browser.element("#firstName").type("Dan")
    browser.element("#lastName").type("Roz")
    browser.element('#userEmail').type('dr@olololo.net')
    browser.element('#age').type('18')
    browser.element('#salary').type('100000')
    browser.element('#department').type('VIVIFY')
    browser.element('#submit').click()
    browser.element('#edit-record-2').click()
    browser.element("#firstName").clear().type("NotDab")
    browser.element("#lastName").clear().type("NotRoz")
    browser.element('#userEmail').clear().type('Notdr@olololo.net')
    browser.element('#age').clear().type('24')
    browser.element('#salary').clear().type('200000')
    browser.element('#department').clear().type('NOTVIVIFY')
    browser.element('#submit').click()
    browser.element('#delete-record-3').click()
