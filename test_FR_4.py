from playwright.sync_api import Playwright, Page, expect


def test_case_id_4(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://app.linkedbusiness.eu/home")
    page.get_by_role("button", name="ΕΙΣΟΔΟΣ ΣΤΟ KYC").click()

    context.close()
    browser.close()