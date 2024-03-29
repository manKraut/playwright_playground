import configparser

from playwright.sync_api import Playwright, Page, expect


def test_case_id_17(playwright: Playwright):
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

    page.get_by_text("B2B").click()
    page.get_by_role("button", name="Είσοδος στην Πλατφόρμα").click()
    option = page.get_by_placeholder("Αναζήτηση Αγοράς...").count()




    assert option == config['PAGE']['num_of_available_markets']

    context.close()
    browser.close()
