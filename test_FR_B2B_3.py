import configparser

from playwright.sync_api import Playwright, Page, expect


def test_case_id_13(playwright: Playwright):
    config = configparser.ConfigParser()
    config.read('config.env')
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(config['PAGE']['UrlB2B'])
    geo_filter = page.get_by_role("button", name="Γεωγραφία").count()
    assert geo_filter == 1

    context.close()
    browser.close()