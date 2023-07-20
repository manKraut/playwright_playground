import configparser

from playwright.sync_api import Playwright, Page, expect

def test_case_id_55(playwright: Playwright):
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

    page.get_by_text("KYC (KNOW YOUR CUSTOMER)").click()
    page.get_by_role("button", name="Είσοδος στην Πλατφόρμα").click()
    page.wait_for_timeout(2000)

    # Enter notifications and search for option that refers to KYC
    page.locator("app-header").get_by_role("img").nth(3).click()
    page.get_by_role("link", name="Δείτε περισσότερα...").click()
    button_kyc_notifications = page.get_by_role("button", name="Υπηρεσία Know Your Customer").inner_text()

    assert button_kyc_notifications == "Υπηρεσία Know Your Customer"

    context.close()
    browser.close()

