import allure
import json
from pages.text_box_page import TextBoxPage


@allure.title("Успешное заполнение Text Box")
def test_fill_text_box():
    # 1. Загружаем тестовые данные
    with open("data/users.json", "r") as f:
        student_data = json.load(f)["student"]

    # 2. Создаём объект страницы
    text_box_page = TextBoxPage()

    # 3. Открываем страницу
    text_box_page.open()

    # 4. Заполняем форму
    text_box_page.fill_form(
        full_name=f"{student_data['first_name']} {student_data['last_name']}",
        email=student_data['email'],
        current_address=student_data['address'],
        permanent_address=student_data['address']
    )

    # 5. Проверяем результат
    text_box_page.should_have_result(
        full_name=f"{student_data['first_name']} {student_data['last_name']}",
        email=student_data['email'],
        current_address=student_data['address'],
        permanent_address=student_data['address']
    )