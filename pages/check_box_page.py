from selene import browser, have, command
import allure

class CheckBoxPage:
    def open(self):
        from conf.config import BASE_URL
        with allure.step("Открыть страницу Check Box"):
            browser.open(f"{BASE_URL}/checkbox")
        return self

    def expand_all_folders(self):
        with allure.step("Развернуть все папки"):
            browser.element(".rct-option-expand-all").click()
        return self

    def check_option(self, option_name: str):
        with allure.step(f"Выбрать чекбокс '{option_name}'"):
            browser.element(f"//span[text()='{option_name}']/preceding-sibling::span[@class='rct-checkbox']").click()
        return self

    def assert_option_checked(self, option_name: str):
        with allure.step(f"Проверить, что чекбокс '{option_name}' выбран"):
            checkbox_input = browser.element(f"//span[text()='{option_name}']/preceding-sibling::span/input")
            checkbox_input.should(have.attribute('checked'))
        return self