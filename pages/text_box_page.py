import allure
from selene import browser, have, command


class TextBoxPage:

    @allure.step("Открыть страницу Text Box")
    def open(self):
        browser.open("https://demoqa.com/text-box")
        browser.driver.execute_script("document.querySelector('#fixedban')?.remove()")
        browser.driver.execute_script("document.querySelector('footer')?.remove()")
        return self

    @allure.step("Заполнить форму Text Box")
    def fill_form(self, full_name, email, current_address, permanent_address):
        browser.element('#userName').type(full_name)
        browser.element('#userEmail').type(email)
        browser.element('#currentAddress').type(current_address)
        browser.element('#permanentAddress').type(permanent_address)
        browser.element('#submit').perform(command.js.click)
        return self

    @allure.step("Проверить результат")
    def should_have_result(self, full_name, email, current_address, permanent_address):
        browser.element('#output').should(have.text(full_name))
        browser.element('#output').should(have.text(email))
        browser.element('#output').should(have.text(current_address))
        browser.element('#output').should(have.text(permanent_address))
        return self


text_box_page = TextBoxPage()