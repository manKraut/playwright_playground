import configparser

from playwright.sync_api import Playwright, Page, expect


def test_case_id_16(playwright: Playwright):
    config = configparser.ConfigParser()
    config.read('config.env', 'utf-8')
    browser = playwright.chromium.launch(headless=False)
    # context = browser.new_context()
    context = browser.new_context(
        http_credentials={"username": config['HTTP CREDS']['username'],
                          "password": config['HTTP CREDS']['password']}
    )
    page = context.new_page()
    page.goto(config['PAGE']['Url'])

    # Verify box availability
    page.get_by_text("B2B").click()
    page.get_by_role("button", name="Είσοδος στην Πλατφόρμα").click()
    box_availability = page.get_by_placeholder("Επιλέξτε Αγορά...").count()
    assert box_availability == 1

    context.close()
    browser.close()
