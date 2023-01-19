import configparser

from playwright.sync_api import Playwright, Page, expect


def test_case_id_11(playwright: Playwright):
    config = configparser.ConfigParser()
    config.read('config.env')
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(config['PAGE']['UrlB2B'])
    box_visibility = page.get_by_placeholder("Αναζήτηση Αγοράς...").count()
    assert box_visibility == 1

    context.close()
    browser.close()
