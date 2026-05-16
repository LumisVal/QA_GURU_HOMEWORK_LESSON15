import allure
import json
from pages.web_tables_page import WebTablesPage

def load_web_user():
    with open("data/web_user.json", "r", encoding="utf-8") as f:
        return json.load(f)

@allure.title("Добавление новой записи в Web Tables")
def test_add_new_record():
    user = load_web_user()
    page = WebTablesPage()
    page.open()
    page.add_new_record(user)
    page.assert_record_exists(user["first_name"], user["last_name"])