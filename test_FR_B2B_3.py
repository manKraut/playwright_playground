from playwright.sync_api import Playwright, Page, expect


def test_case_id_13(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://app.linkedbusiness.eu/b2b-dashboard")
    geo_filter = page.get_by_role("button", name="Γεωγραφία").count()
    assert geo_filter == 1

    context.close()
    browser.close()