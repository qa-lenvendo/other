from selene import browser, have, be

def test_homework():

    browser.open('/automation-practice-form')

    browser.element('[id="firstName"]').send_keys('Ivan')
    browser.element('[id="lastName"]').send_keys('Ivanov')
    browser.element('[id="userEmail"]').send_keys('r@ya.com')
    browser.element('[name="gender"][value=Male]').double_click()
    browser.element('[id="userNumber"]').send_keys('+7777777777')

    browser.element('[id="dateOfBirthInput"]').click()
    browser.element('.react-datepicker__year-select').click().element('[value="1990"]').click()
    browser.element('.react-datepicker__month-select').click().element('[value="2"]').click()
    browser.element('.react-datepicker__day--022').click()

    browser.element('#subjectsInput').click().send_keys('Maths').press_enter()

    browser.element('[id="hobbies-checkbox-1"]').double_click()

    # browser.element('id="uploadPicture"').click()

    browser.element('[id="currentAddress"]').send_keys('Test-city, test street, test house 2')

    browser.element('[id="state"]').click()
    browser.element('[id="state"]').send_keys('U').press_enter()


    ...