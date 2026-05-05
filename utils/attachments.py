import allure
from selene import browser


def attach_screenshot():
    allure.attach(
        browser.driver.get_screenshot_as_png(),
        name="screenshot",
        attachment_type=allure.attachment_type.PNG
    )


def attach_page_source():
    allure.attach(
        browser.driver.page_source,
        name="page_source",
        attachment_type=allure.attachment_type.HTML
    )


def attach_browser_logs():
    try:
        logs = browser.driver.get_log("browser")
        log_text = "\n".join(str(log) for log in logs)
        allure.attach(
            log_text,
            name="browser_logs",
            attachment_type=allure.attachment_type.TEXT
        )
    except Exception:
        pass


def attach_video(session_id):
    video_url = f"https://selenoid.autotests.cloud/video/{session_id}.mp4"
    allure.attach(
        f'<html><body><video width="100%" height="100%" controls autoplay>'
        f'<source src="{video_url}" type="video/mp4"></video></body></html>',
        name="video",
        attachment_type=allure.attachment_type.HTML
    )