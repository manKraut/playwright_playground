import configparser

from playwright.sync_api import Playwright, sync_playwright, expect


def test_case_id_46(playwright: Playwright) -> None:
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

    # Go to B2B Sales Leads and select market
    page.get_by_placeholder("Επιλέξτε Αγορά...").click()
    page.get_by_role("option", name="Εστιατόρια").click()

    # Press the button "Δείτε τις υπόλοιπες Χ"
    page.locator('button:has-text("Αποκτήστε τις υπόλοιπες")').click()
    order_id = page.url.split('=')[2]

    assert order_id == '80133'

    context.close()
    browser.close()
