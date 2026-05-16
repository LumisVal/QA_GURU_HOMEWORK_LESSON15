import os
import time
from pathlib import Path

import allure
import pytest
import requests
from dotenv import load_dotenv
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Загружаем переменные из .env файла, который лежит в корне проекта
dotenv_path = Path(__file__).parent.parent / '.env'
load_dotenv(dotenv_path=dotenv_path)


@pytest.fixture(scope='function', autouse=True)
def setup_browser(request):

    options = Options()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    remote_url = os.getenv("REMOTE_URL")
    driver = None

    if remote_url:
        # Удалённый запуск через Selenoid
        video_name = f"{request.node.name}.mp4"
        options.set_capability("browserName", os.getenv("BROWSER_NAME", "chrome"))
        options.set_capability("browserVersion", os.getenv("BROWSER_VERSION", "128.0"))
        options.set_capability(
            "selenoid:options",
            {
                "enableVNC": True,
                "enableVideo": True,
                "videoName": video_name,
                "name": request.node.name,
            }
        )
        driver = webdriver.Remote(command_executor=remote_url, options=options)
        request.node.video_name = video_name
    else:
        # Локальный запуск (для отладки)
        driver = webdriver.Chrome(options=options)

    browser.config.driver = driver
    # Базовый URL можно задать, но в Page Object вы его не используете – опционально
    browser.config.base_url = os.getenv("BASE_URL", "https://demoqa.com")

    yield

    # Финальный скриншот (для успешных тестов – полезно для отчёта)
    try:
        allure.attach(
            browser.driver.get_screenshot_as_png(),
            name="final_screenshot",
            attachment_type=allure.attachment_type.PNG,
        )
    except Exception:
        pass

    browser.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        try:
            allure.attach(
                browser.driver.get_screenshot_as_png(),
                name=f"screenshot_{item.name}",
                attachment_type=allure.attachment_type.PNG,
            )
        except Exception:
            pass


@pytest.fixture(scope="function", autouse=True)
def attach_video_after_test(request):

    yield
    remote_url = os.getenv("REMOTE_URL")
    video_name = getattr(request.node, "video_name", None)
    if not remote_url or not video_name:
        return

    # Формируем URL для скачивания видео
    base_url = remote_url.split("/wd/hub")[0]
    video_url = f"{base_url}/video/{video_name}"

    # Ждём, пока видео станет доступно (максимум 15 секунд)
    for _ in range(15):
        try:
            resp = requests.head(video_url, timeout=2)
            if resp.status_code == 200:
                break
        except requests.RequestException:
            pass
        time.sleep(1)
    else:
        allure.attach(
            "Video file not found or not ready",
            name="video_error",
            attachment_type=allure.attachment_type.TEXT,
        )
        return

    # Скачиваем и прикрепляем видео
    try:
        response = requests.get(video_url, timeout=20)
        if response.status_code == 200:
            allure.attach(
                response.content,
                name=video_name,
                attachment_type="video/mp4",
                extension="mp4",
            )
        else:
            allure.attach(
                video_url,
                name="video_url",
                attachment_type=allure.attachment_type.URI_LIST,
            )
    except Exception as e:
        allure.attach(str(e), name="video_attach_error", attachment_type=allure.attachment_type.TEXT)