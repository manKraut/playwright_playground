import configparser

from playwright.sync_api import Playwright, Page, expect

def test_case_id_2(playwright: Playwright):
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

    # Successful Login with Facebook
    page.get_by_role("button", name="Είσοδος/Εγγραφή").click()
    page.locator("#btn-fb").click()
    page.get_by_role("button", name="Decline optional cookies").click()
    page.get_by_placeholder("Email or phone number").fill(config['USER SOCIALS']['email'])
    page.get_by_placeholder("Password").fill(config['USER SOCIALS']['password'])
    page.get_by_role("button", name="Log In").click()
    page.wait_for_timeout(10000)
    url = page.url

    assert url == "https://front.linkedbusiness.eu/"

    context.close()
    browser.close()
