from playwright.sync_api import Playwright, sync_playwright, expect


def test_case_id_34(playwright: Playwright) -> None:
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

    # Navigate to relevant alert
    page.locator("app-header").get_by_role("img").nth(3).click()
    page.get_by_role("heading", name="Market").click()
    page.get_by_role("button", name="Μετάβαση στα Στοιχεία").click()
    expect(page).to_have_url('https://app.linkedbusiness.eu/b2b-dashboard/b2b-markets-view')

    context.close()
    browser.close()
