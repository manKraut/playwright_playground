import configparser

from playwright.sync_api import Playwright, sync_playwright, expect


def test_case_id_39(playwright: Playwright) -> None:
    config = configparser.ConfigParser()
    config.read('config.env', 'utf-8')
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(config['PAGE']['Url'])

    # Successful Login
    page.get_by_role("button", name="Είσοδος").click()
    page.get_by_placeholder("Email").click()
    page.get_by_placeholder("Email").fill(config['USER']['Email'])
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill(config['USER']['Password'])
    page.get_by_role("button", name="Είσοδος").click()

    # Select a market and verify the incorporation date filter is available
    page.get_by_role("option", name=config['EXAMPLES']['example_market']).click()
    page.get_by_role("button", name="Αναζήτηση").click()
    incorporation_date_filter_button = page.get_by_role("button", name="Μήνας Ίδρυσης")

    assert incorporation_date_filter_button is not None
