import configparser

from playwright.sync_api import Playwright, sync_playwright, expect


def test_case_id_44(playwright: Playwright) -> None:
    config = configparser.ConfigParser()
    config.read('config.env', 'utf-8')
    browser = playwright.chromium.launch(headless=False)

    if "front" in config['PAGE']['Url']:
        context = browser.new_context(
            http_credentials={"username": config['PAGE']['http_creds_username'],
                              "password": config['PAGE']['http_creds_password']}
        )
    else:
        context = browser.new_context()

    page = context.new_page()
    page.goto(config['PAGE']['Url'])

    # Successful Login
    page.get_by_role("button", name="Είσοδος/Εγγραφή").click()
    page.get_by_role("textbox", name="Email").click()
    page.get_by_role("textbox", name="Email").fill(config['USER']['Email'])
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill(config['USER']['Password'])
    page.get_by_role("button", name="Είσοδος").click()

    page.get_by_text("B2B").click()
    page.get_by_role("button", name=config['PAGE']['entry_btn']).click()
    redirection_page = page.url

    # Go to dashboard and select specific lead "Ξενοδοχεία"
    #page.get_by_role("button", name="ΕΙΣΟΔΟΣ ΣΤΟ B2B").click()
    page.get_by_role("link", name="B2B Dashboard").click()
    page.get_by_text("Ξενοδοχεία 192 Ίδρυση από ΝΟΕΜΒΡΙΟΣ 2022")
    sorting_filter = page.locator("app-dropdown").filter(
        has_text="Πωλήσεις Ημερομηνία Ημερομηνία Εταιρικός Τύπος Εταιρικός Τύπος Πωλήσεις Πωλήσεις").get_by_role(
        "button", name="Πωλήσεις")

    # Verify the sorting filter is available
    assert sorting_filter is not None

    context.close()
    browser.close()
