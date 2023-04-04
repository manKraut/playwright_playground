import configparser

from playwright.sync_api import Playwright, Page, expect


def test_case_id_17(playwright: Playwright):
    config = configparser.ConfigParser()
    config.read('config.env', 'utf-8')
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(config['PAGE']['UrlB2B'])
    page.get_by_placeholder("Αναζήτηση Αγοράς...").click()
    available_markets = page.get_by_role("option").count()
    assert available_markets == config['PAGE']['num_of_available_markets']

    context.close()
    browser.close()
