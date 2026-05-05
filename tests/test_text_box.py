import allure
from data.users import student
from pages.text_box_page import TextBoxPage

text_box_page = TextBoxPage()


@allure.title("Успешное заполнение Text Box")
def test_fill_text_box():
    text_box_page.open().fill_form(
        full_name=student.first_name + " " + student.last_name,
        email=student.email,
        current_address=student.address,
        permanent_address=student.address
    ).should_have_result(
        full_name=student.first_name + " " + student.last_name,
        email=student.email,
        current_address=student.address,
        permanent_address=student.address
    )