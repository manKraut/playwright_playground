import configparser

from playwright.sync_api import Playwright, Page, expect


def test_case_id_2(playwright: Playwright):
    config = configparser.ConfigParser()
    config.read('config.env', 'utf-8')
    browser = playwright.chromium.launch(headless=False)
    # context = browser.new_context()
    context = browser.new_context(
        http_credentials={"username": "lbUser", "password": "lbP4ss2022!"}
    )
    page = context.new_page()
    page.goto(config['PAGE']['Url'])



    context.close()
    browser.close()