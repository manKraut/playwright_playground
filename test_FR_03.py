import configparser

from playwright.sync_api import Playwright, Page, expect

def test_case_id_3(playwright: Playwright):
    config = configparser.ConfigParser()
    config.read('config.env', 'utf-8')
    browser = playwright.firefox.launch(headless=False)
    # context = browser.new_context()
    context = browser.new_context(
        http_credentials={"username": config['HTTP CREDS']['username'],
                          "password": config['HTTP CREDS']['password']}
    )
    page = context.new_page()
    page.goto(config['PAGE']['Url'])

    # Navigate to welcome page and enter B2B
    page.get_by_text("KNOW YOUR CUSTOMER").click()
    page.get_by_role("button", name="Είσοδος στην Πλατφόρμα").click()
    redirection_page = page.url

    assert redirection_page == "https://front.linkedbusiness.eu/kyc-dashboard?type=0"

    context.close()
    browser.close()