from selene import browser, have, be
import os

def test_homework():

    browser.open('/automation-practice-form')

    browser.element('[id="firstName"]').send_keys('Ivan')
    browser.element('[id="lastName"]').send_keys('Ivanov')
    browser.element('[id="userEmail"]').send_keys('r@ya.com')
    browser.element('[name="gender"][value=Male]').double_click()
    browser.element('[id="userNumber"]').send_keys('7777777777')

    browser.element('[id="dateOfBirthInput"]').click()
    browser.element('.react-datepicker__year-select').click().element('[value="1990"]').click()
    browser.element('.react-datepicker__month-select').click().element('[value="2"]').click()
    browser.element('.react-datepicker__day--022').click()

    browser.element('#subjectsInput').click().send_keys('Maths').press_enter()

    browser.element('label[for="hobbies-checkbox-1"]').click()

    browser.element('#uploadPicture').send_keys(os.getcwd() + '/test.png')

    browser.element('[id="currentAddress"]').send_keys('Test-city, test street, test house 2')

    browser.element('#state').click()
    browser.all('[id^=react-select][id*=option]').element_by(have.exact_text('NCR')).click()
    browser.element('#react-select-4-input').type('Delhi').press_enter()

    browser.element('#submit').press_enter()

    browser.all('tbody tr').should(have.exact_texts(
        'Student Name Ivan Ivanov', 'Student Email r@ya.com', 'Gender Male', 'Mobile 7777777777',
        'Date of Birth 22 March,1990', 'Subjects Maths', 'Hobbies Sports',
        'Picture test.png', 'Address Test-city, test street, test house 2',
        'State and City NCR Delhi'))

