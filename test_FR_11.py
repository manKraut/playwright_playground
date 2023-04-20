import configparser

from playwright.sync_api import Playwright, sync_playwright, expect


def test_case_id_12(playwright: Playwright) -> None:
    config = configparser.ConfigParser()
    config.read('config.env', 'utf-8')
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    # context = browser.new_context(
    #     http_credentials={"username": "lbUser", "password": "lbP4ss2022!"}
    # )
    page = context.new_page()
    page.goto(config['PAGE']['Url'])

    # Successful Login
    page.get_by_role("button", name="Είσοδος/Εγγραφή").click()
    page.get_by_role("textbox", name="Email").click()
    page.get_by_role("textbox", name="Email").fill(config['USER']['Email'])
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill(config['USER']['Password'])
    page.get_by_role("button", name="Είσοδος").click()

    # Go to user's profile basic info and put a valid VAT number
    page.get_by_text("B2B").click()
    page.get_by_role("button", name="Είσοδος στην Πλατφόρμα").click()
    page.locator("app-header").get_by_role("img").nth(3).click()
    page.get_by_role("button", name="Βασικές Πληροφορίες").click()
    page.get_by_placeholder("Α.Φ.Μ.").click()
    page.get_by_placeholder("Α.Φ.Μ.").fill("800950289")
    tick_validator_image = page.locator("#vat").get_by_role("img")

    assert tick_validator_image is not None

    context.close()
    browser.close()


