import allure
from selene import browser, have


@allure.title("Успешное добавление новой записи в Web Tables")
def test_add_new_record_in_web_tables():
    browser.open("https://demoqa.com/webtables")

    browser.driver.execute_script("document.querySelector('#fixedban')?.remove()")
    browser.driver.execute_script("document.querySelector('footer')?.remove()")

    browser.element("#addNewRecordButton").click()

    browser.element("#firstName").type("Leonid")
    browser.element("#lastName").type("Chaliy")
    browser.element("#userEmail").type("leonid@example.com")
    browser.element("#age").type("25")
    browser.element("#salary").type("150000")
    browser.element("#department").type("QA")
    browser.element("#submit").click()

    browser.element(".web-tables-wrapper").should(have.text("Leonid"))
    browser.element(".web-tables-wrapper").should(have.text("Chaliy"))
    browser.element(".web-tables-wrapper").should(have.text("leonid@example.com"))
    browser.element(".web-tables-wrapper").should(have.text("25"))
    browser.element(".web-tables-wrapper").should(have.text("150000"))
    browser.element(".web-tables-wrapper").should(have.text("QA"))


@allure.title("Успешный поиск записи в Web Tables")
def test_search_record_in_web_tables():
    browser.open("https://demoqa.com/webtables")

    browser.driver.execute_script("document.querySelector('#fixedban')?.remove()")
    browser.driver.execute_script("document.querySelector('footer')?.remove()")

    browser.element("#searchBox").type("Cierra")

    browser.element(".web-tables-wrapper").should(have.text("Cierra"))
    browser.element(".web-tables-wrapper").should(have.text("Vega"))