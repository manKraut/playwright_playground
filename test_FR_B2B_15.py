from playwright.sync_api import Playwright, Page, expect


def test_case_id_29(playwright: Playwright):
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

    page.get_by_role("button", name="ΕΙΣΟΔΟΣ ΣΤΟ B2B").click()

    page.get_by_role("link", name="B2B Dashboard").click()
    # click on first purchased lead
    page.get_by_text("Ξενοδοχεία 17").first.click()
    page.goto("https://app.linkedbusiness.eu/b2b-dashboard/b2b-my-leads?subscriptionId=106")
    # click at a point on map
    page.locator("div:nth-child(3) > div:nth-child(4)").click()
    # get the name of the company, showing on the map
    name_on_map = page.get_by_role("heading", name="CENTRAL BEACH HOTEL ΜΟΝΟΠΡΟΣΩΠΗ ΙΔΙΩΤΙΚΗ ΚΕΦΑΛΑΙΟΥΧΙΚΗ ΕΤΑΙΡΙΑ")

    assert name_on_map is not None

    context.close()
    browser.close()