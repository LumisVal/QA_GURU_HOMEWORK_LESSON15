import allure
from pages.check_box_page import CheckBoxPage

@allure.title("Выбор чекбокса Home")
def test_check_home():
    page = CheckBoxPage()
    page.open()
    page.expand_all_folders()
    page.check_option("Home")
    page.assert_option_checked("Home")