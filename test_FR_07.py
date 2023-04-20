import configparser

from playwright.sync_api import Playwright, Page, expect


def test_case_id_7(playwright: Playwright):
    config = configparser.ConfigParser()
    config.read('config.env', 'utf-8')
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    # context = browser.new_context(
    #     http_credentials={"username": "lbUser", "password": "lbP4ss2022!"}
    # )
    page = context.new_page()
    page.goto(config['PAGE']['Url'])

    # Fill in the email and check if proper message is prompt
    page.get_by_role("button", name="Είσοδος/Εγγραφή").click()
    page.get_by_role("textbox", name="Email").click()
    page.get_by_role("textbox", name="Email").fill(config['USER']['Email'])

    page.get_by_role("button", name="Ξέχασα το password").click()
    message = page.get_by_text("Μόλις σας στείλαμε Email για να αλλάξετε τον κωδικό σας.")

    assert message is not None

    context.close()
    browser.close()
