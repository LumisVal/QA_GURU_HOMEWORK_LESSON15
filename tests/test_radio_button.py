import allure
from selene import browser, have


@allure.title("Успешный выбор radio button Yes")
def test_select_yes_radio_button():
    browser.open("https://demoqa.com/radio-button")

    browser.driver.execute_script("document.querySelector('#fixedban')?.remove()")
    browser.driver.execute_script("document.querySelector('footer')?.remove()")

    browser.element("label[for='yesRadio']").click()
    browser.element(".text-success").should(have.exact_text("Yes"))


@allure.title("Успешный выбор radio button Impressive")
def test_select_impressive_radio_button():
    browser.open("https://demoqa.com/radio-button")

    browser.driver.execute_script("document.querySelector('#fixedban')?.remove()")
    browser.driver.execute_script("document.querySelector('footer')?.remove()")

    browser.element("label[for='impressiveRadio']").click()
    browser.element(".text-success").should(have.exact_text("Impressive"))