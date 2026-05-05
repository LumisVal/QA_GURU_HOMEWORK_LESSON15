import allure
from selene import browser, have


@allure.title("Успешный выбор checkbox Home")
def test_select_desktop_checkbox():
    browser.open("https://demoqa.com/checkbox")

    browser.driver.execute_script("document.querySelector('#fixedban')?.remove()")
    browser.driver.execute_script("document.querySelector('footer')?.remove()")

    browser.element("h1").should(have.exact_text("Check Box"))

    # раскрываем Home
    browser.element(".rc-tree-switcher").click()

    # выбираем чекбокс
    browser.element(".rc-tree-checkbox").click()

    # проверка результата
    browser.element(".text-success").should(have.text("home"))