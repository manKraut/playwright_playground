import configparser

from playwright.sync_api import Playwright, Page, expect


def test_case_id_16(playwright: Playwright):
    config = configparser.ConfigParser()
    config.read('config.env', 'utf-8')
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(config['PAGE']['UrlB2B'])

    # Verify box availability
    box_availability = page.get_by_placeholder("Αναζήτηση Αγοράς...").count()
    assert box_availability == 1

    context.close()
    browser.close()
