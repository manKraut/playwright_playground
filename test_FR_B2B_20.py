import configparser

from playwright.sync_api import Playwright, sync_playwright, expect


def test_case_id_35(playwright: Playwright) -> None:
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

    # Navigate to relevant alert
    page.wait_for_timeout(2000)
    page.locator("app-header").get_by_role("img").nth(3).click()
    page.get_by_text("Ενημέρωση Παραγγελίας για B2B Subscription 11/07/2023 12:21").click()
    page.get_by_role("button", name="Μετάβαση στα Στοιχεία").click()
    page.wait_for_timeout(5000)
    redirection_url = page.url

    assert redirection_url == "https://front.linkedbusiness.eu/b2b-dashboard/b2b-markets-view"

    context.close()
    browser.close()
