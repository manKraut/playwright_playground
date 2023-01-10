from playwright.sync_api import Playwright, Page, expect


def test_case_id_15(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://app.linkedbusiness.eu/b2b-dashboard")
    page.get_by_placeholder("Αναζήτηση Αγοράς...").click()
    page.get_by_role("option", name="Ξενοδοχεία (8.083)").click()
    page.get_by_role("button", name="Αναζήτηση").click()
    number_of_results = page.locator("").count()
    assert number_of_results == 5

    # name, address, GEMI number, incorporation date, main activity and contact details