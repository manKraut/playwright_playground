import configparser

from playwright.sync_api import Playwright, Page, expect


def test_case_id_8(playwright: Playwright):
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

    # Successful Login and access platform
    page.get_by_role("button", name="Είσοδος/Εγγραφή").click()
    page.get_by_role("textbox", name="Email").fill(config['USER LOGIN']['email'])
    page.get_by_role("textbox", name="Password").fill(config['USER LOGIN']['password'])
    page.get_by_role("button", name="Είσοδος").click()
    page.get_by_role("button", name="Είσοδος στην Πλατφόρμα").click()

    # Access purchased subscriptions
    page.locator("app-header").get_by_role("img").nth(3).click()
    page.get_by_role("button", name="Συνδρομές - Πακέτα Report").click()
    subscription = page.get_by_text("Subscription: Pro").inner_text()

    assert subscription == "Subscription: Pro"

    context.close()
    browser.close()
