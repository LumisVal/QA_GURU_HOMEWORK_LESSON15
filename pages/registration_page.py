import os

from selene import browser, have, command


class RegistrationPage:

    def open(self):
        browser.open("https://demoqa.com/automation-practice-form")
        browser.driver.execute_script("document.querySelector('#fixedban')?.remove()")
        browser.driver.execute_script("document.querySelector('footer')?.remove()")
        return self

    def choose_gender(self, gender):
        gender_map = {
            'Male': '1',
            'Female': '2',
            'Other': '3',
        }

        gender_value = gender_map[gender]
        gender_element = browser.element(f'label[for="gender-radio-{gender_value}"]')
        gender_element.perform(command.js.scroll_into_view)
        gender_element.perform(command.js.click)
        return self

    def should_have_form_title(self):
        browser.element('.practice-form-wrapper h5').should(
            have.exact_text('Student Registration Form')
        )
        return self

    def should_have_basic_fields(self):
        browser.element('#firstName').should(have.attribute('placeholder').value('First Name'))
        browser.element('#lastName').should(have.attribute('placeholder').value('Last Name'))
        browser.element('#userEmail').should(have.attribute('placeholder').value('name@example.com'))
        browser.element('#userNumber').should(have.attribute('placeholder').value('Mobile Number'))
        return self

    def register_required_fields_only(self, student):
        browser.element('#firstName').type(student.first_name)
        browser.element('#lastName').type(student.last_name)

        self.choose_gender(student.gender)

        browser.element('#userNumber').type(student.phone)

        browser.element('#submit').perform(command.js.scroll_into_view)
        browser.element('#submit').perform(command.js.click)
        return self

    def register(self, student):
        browser.element('#firstName').type(student.first_name)
        browser.element('#lastName').type(student.last_name)
        browser.element('#userEmail').type(student.email)

        self.choose_gender(student.gender)

        browser.element('#userNumber').type(student.phone)

        browser.element('#dateOfBirthInput').click()

        month_map = {
            'January': '0',
            'February': '1',
            'March': '2',
            'April': '3',
            'May': '4',
            'June': '5',
            'July': '6',
            'August': '7',
            'September': '8',
            'October': '9',
            'November': '10',
            'December': '11',
        }

        browser.element('.react-datepicker__month-select').click()
        browser.element(f'option[value="{month_map[student.birth_month]}"]').click()

        browser.element('.react-datepicker__year-select').click()
        browser.element(f'option[value="{student.birth_year}"]').click()

        browser.element(
            f'.react-datepicker__day--0{student.birth_day}:not(.react-datepicker__day--outside-month)'
        ).click()

        browser.element('#subjectsInput').type(student.subject).press_enter()

        browser.element('label[for="hobbies-checkbox-1"]').perform(command.js.scroll_into_view)
        browser.element('label[for="hobbies-checkbox-1"]').perform(command.js.click)

        if hasattr(student, 'picture_path') and student.picture_path:
            browser.element('#uploadPicture').send_keys(os.path.abspath(student.picture_path))

        browser.element('#currentAddress').type(student.address)

        browser.element('#state').perform(command.js.scroll_into_view)
        browser.element('#state').click()
        browser.element('#react-select-3-input').type(student.state).press_enter()

        browser.element('#city').click()
        browser.element('#react-select-4-input').type(student.city).press_enter()

        browser.element('#submit').perform(command.js.scroll_into_view)
        browser.element('#submit').perform(command.js.click)

        return self

    def should_have_success_modal(self):
        browser.element('#example-modal-sizes-title-lg').should(
            have.exact_text('Thanks for submitting the form')
        )
        return self

    def should_have_registered(self, student):
        browser.element('#example-modal-sizes-title-lg').should(
            have.exact_text('Thanks for submitting the form')
        )

        browser.element('.table-responsive').should(have.text(student.first_name))
        browser.element('.table-responsive').should(have.text(student.last_name))
        browser.element('.table-responsive').should(have.text(student.email))
        browser.element('.table-responsive').should(have.text(student.gender))
        browser.element('.table-responsive').should(have.text(student.phone))
        browser.element('.table-responsive').should(have.text(student.subject))
        browser.element('.table-responsive').should(have.text(student.address))
        browser.element('.table-responsive').should(have.text(student.state))
        browser.element('.table-responsive').should(have.text(student.city))

        return self