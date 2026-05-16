from selene import browser, have
import allure

class WebTablesPage:
    def open(self):
        from conf.config import BASE_URL
        with allure.step("Открыть страницу Web Tables"):
            browser.open(f"{BASE_URL}/webtables")
        return self

    def add_new_record(self, user: dict):
        with allure.step(f"Добавить запись {user['first_name']} {user['last_name']}"):
            browser.element("#addNewRecordButton").click()
            browser.element("#firstName").type(user["first_name"])
            browser.element("#lastName").type(user["last_name"])
            browser.element("#userEmail").type(user["email"])
            browser.element("#age").type(str(user["age"]))
            browser.element("#salary").type(str(user["salary"]))
            browser.element("#department").type(user["department"])
            browser.element("#submit").click()
        return self

    def assert_record_exists(self, first_name: str, last_name: str):
        with allure.step(f"Проверить, что запись {first_name} {last_name} существует"):
            browser.element(f"//div[text()='{first_name} {last_name}']").should(have.exact_text(f"{first_name} {last_name}"))
        return self