import configparser

from playwright.sync_api import Playwright, sync_playwright, expect


def test_case_id_8(playwright: Playwright) -> None:
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

    # Access purchased packages
    page.locator("app-header").get_by_role("img").nth(4).click()
    page.get_by_role("button", name="Συνδρομές - Πακέτα Report").click()
    subscriptions_tab = page.locator("label").filter(has_text="Συνδρομές")
    reports_tab = page.get_by_text("Πακέτο Report")

    assert subscriptions_tab is not None
    assert reports_tab is not None

    context.close()
    browser.close()
