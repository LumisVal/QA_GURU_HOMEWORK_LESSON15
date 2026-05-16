from selene import browser, have
import allure

class RadioButtonPage:
    def open(self):
        from conf.config import BASE_URL
        with allure.step("Открыть страницу Radio Button"):
            browser.open(f"{BASE_URL}/radio-button")
        return self

    def select_radio(self, choice: str):
        with allure.step(f"Выбрать радио-кнопку '{choice}'"):
            browser.element(f"//label[@for='{choice.lower()}Radio']").click()
        return self

    def assert_radio_selected(self, choice: str):
        with allure.step(f"Проверить, что выбрана кнопка '{choice}'"):
            radio = browser.element(f"#{'yes' if choice == 'Yes' else choice.lower()}Radio")
            radio.should(have.attribute('checked'))
        return self