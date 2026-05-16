import allure
import json
from pages.registration_page import RegistrationPage

def load_student():
    with open("data/student.json", "r", encoding="utf-8") as f:
        return json.load(f)

student_data = load_student()
registration_page = RegistrationPage()


@allure.title("Успешная полная регистрация студента")
def test_student_registration():
    registration_page.open()
    registration_page.register(student_data)
    registration_page.should_have_registered(student_data)


@allure.title("Страница формы успешно открывается")
def test_form_page_should_open():
    registration_page.open()
    registration_page.should_have_form_title()


@allure.title("Основные поля формы отображаются")
def test_basic_fields_should_be_visible():
    registration_page.open()
    registration_page.should_have_basic_fields()


@allure.title("Можно выбрать пол в форме")
def test_gender_can_be_selected():
    registration_page.open()
    registration_page.choose_gender(student_data["gender"])
    # Добавленная проверка
    registration_page.should_have_gender_selected(student_data["gender"])


@allure.title("Форма отправляется с обязательными полями")
def test_required_fields_registration():
    registration_page.open()
    registration_page.register_required_fields_only(student_data)
    registration_page.should_have_success_modal()