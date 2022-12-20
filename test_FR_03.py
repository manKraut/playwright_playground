from playwright.sync_api import Playwright, Page, expect


def test_case_id_3(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://app.linkedbusiness.eu/home")
    page.get_by_role("button", name="ΕΙΣΟΔΟΣ ΣΤΟ B2B").click()

    context.close()
    browser.close()