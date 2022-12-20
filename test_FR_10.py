from playwright.sync_api import Playwright, Page, expect


def test_case_id_10(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://app.linkedbusiness.eu/home")

    # Successful Login
    page.get_by_role("button", name="Είσοδος").click()
    page.get_by_placeholder("Email").click()
    page.get_by_placeholder("Email").fill("m.adamopoulos@lbsuite.eu")
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("Test123!")
    page.get_by_role("button", name="Είσοδος").click()

    # Search in purchased history
    page.locator("app-header").get_by_role("img").nth(3).click()
    page.get_by_role("button", name="Ιστορικό Αγορών").click()
    page.locator("label").filter(has_text="Συνδρομές - Πακέτα Report").click()
    page.get_by_placeholder("Αναζήτηση...").click()
    page.get_by_placeholder("Αναζήτηση...").fill("B2B")
    # B2B market purchased must exist
    page.get_by_text("B2B Universe, Supermarkets, Παντοπωλεία & Περίπτερα,").click()

    # ---------------------
    context.close()
    browser.close()
