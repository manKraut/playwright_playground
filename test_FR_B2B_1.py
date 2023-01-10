from playwright.sync_api import Playwright, Page, expect


def test_case_id_11(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://app.linkedbusiness.eu/b2b-dashboard")
    box_visibility = page.get_by_placeholder("Αναζήτηση Αγοράς...").count()
    assert box_visibility == 1

    context.close()
    browser.close()
