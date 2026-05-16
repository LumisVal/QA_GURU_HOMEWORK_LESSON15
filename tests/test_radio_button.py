import allure
from pages.radio_button_page import RadioButtonPage

@allure.title("Выбор радио-кнопки Yes")
def test_radio_yes():
    page = RadioButtonPage()
    page.open()
    page.select_radio("Yes")
    page.assert_radio_selected("Yes")