import configparser

from playwright.sync_api import Playwright, sync_playwright, expect


def test_case_id_38(playwright: Playwright) -> None:
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

    # Select a market and verify the turnover filter is available
    page.get_by_placeholder("Επιλέξτε Αγορά...").click()
    page.get_by_role("option", name=config['EXAMPLES']['example_market']).click()
    turnover_filter_button = page.get_by_role("button", name="Πωλήσεις")

    assert turnover_filter_button is not None
