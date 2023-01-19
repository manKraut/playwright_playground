from playwright.sync_api import Playwright, sync_playwright, expect


def test_case_id_35(playwright: Playwright) -> None:
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

    # Go to alert icon and select settings
    page.locator("app-header").get_by_role("img").nth(2).click()
    page.locator(".bi bi-gear-fill settings:has(i)").click()
    # Through the menu uncheck the LB Live alert
    page.locator("#flexSwitchCheckChecked").nth(3).uncheck()

