import configparser

from playwright.sync_api import Playwright, sync_playwright, expect


def test_case_id_36(playwright: Playwright) -> None:
    config = configparser.ConfigParser()
    config.read('config.env', 'utf-8')
    browser = playwright.chromium.launch(headless=False)

    if "front" in config['PAGE']['Url']:
        context = browser.new_context(
            http_credentials={"username": config['PAGE']['http_creds_username'],
                              "password": config['PAGE']['http_creds_password']}
        )
    else:
        context = browser.new_context()

    page = context.new_page()
    page.goto(config['PAGE']['Url'])

    # Successful Login
    page.get_by_role("button", name="Είσοδος/Εγγραφή").click()
    page.get_by_role("textbox", name="Email").fill(config['USER LOGIN']['email'])
    page.get_by_role("textbox", name="Password").fill(config['USER LOGIN']['password'])
    page.get_by_role("button", name="Είσοδος").click()

    page.get_by_text("B2B").click()
    page.get_by_role("button", name="Είσοδος στην Πλατφόρμα").click()

    # Go to alert icon and select settings
    page.wait_for_timeout(2000)
    page.locator("app-header").get_by_role("img").nth(3).click()
    page.goto("https://front.linkedbusiness.eu/notifications/settings")
    # Through the menu uncheck the LB Live alert
    page.get_by_role("switch").nth(1).uncheck()
    page.get_by_role("switch").nth(1).check()

    context.close()
    browser.close()


