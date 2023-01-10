from playwright.sync_api import Playwright, Page, expect


def test_case_id_12(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://app.linkedbusiness.eu/b2b-dashboard")
    page.get_by_placeholder("Αναζήτηση Αγοράς...").click()
    available_markets = page.get_by_role("option").count()
    assert available_markets == 5 # 4 markets and the final option of "Δεν βλέπετε την αγορά που σας ενδιαφέρει;Πατήστε εδώ..."

    context.close()
    browser.close()