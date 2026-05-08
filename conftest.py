import os
import time
import allure
import pytest
import requests
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='function', autouse=True)
def setup_browser(request):
    options = Options()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    remote_url = os.getenv("REMOTE_URL")
    driver = None

    if remote_url:
        video_name = f"{request.node.name}.mp4"

        options.set_capability("browserName", "chrome")
        options.set_capability("browserVersion", os.getenv("BROWSER_VERSION", "128.0"))
        options.set_capability(
            "selenoid:options",
            {
                "enableVNC": True,
                "enableVideo": True,
                "videoName": video_name,
                "name": request.node.name
            }
        )

        driver = webdriver.Remote(
            command_executor=remote_url,
            options=options
        )

        request.node.video_name = video_name
    else:
        driver = webdriver.Chrome(options=options)

    browser.config.driver = driver
    browser.config.base_url = "https://demoqa.com"

    yield

    browser.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        allure.attach(
            browser.driver.get_screenshot_as_png(),
            name=f"screenshot_{item.name}",
            attachment_type=allure.attachment_type.PNG
        )


@pytest.fixture(scope="function", autouse=True)
def attach_video_after_test(request):
    yield

    remote_url = os.getenv("REMOTE_URL")
    video_name = getattr(request.node, "video_name", None)

    if not remote_url or not video_name:
        return

    # ждём, пока Selenoid допишет видео
    time.sleep(3)

    base_url = remote_url.split("/wd/hub")[0]
    video_url = f"{base_url}/video/{video_name}"

    try:
        response = requests.get(video_url, timeout=20)
        if response.status_code == 200:
            allure.attach(
                response.content,
                name=video_name,
                attachment_type="video/mp4",
                extension="mp4"
            )
        else:
            allure.attach(
                video_url,
                name="video_url",
                attachment_type=allure.attachment_type.URI_LIST
            )
    except Exception as e:
        allure.attach(
            str(e),
            name="video_attach_error",
            attachment_type=allure.attachment_type.TEXT
        )