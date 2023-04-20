import configparser

from playwright.sync_api import Playwright, sync_playwright, expect


def test_case_id_41(playwright: Playwright) -> None:
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

    # Click on search box to show available markets in dropdown menu
    #page.get_by_role("button", name="ΕΙΣΟΔΟΣ ΣΤΟ B2B").click()
    page.get_by_placeholder("Αναζήτηση Αγοράς...").click()
    available_markets = page.get_by_role("option").count()

    # verify that the dropdown menu with all markets is still available
    #assert available_markets == str(config['PAGE']['num_of_available_markets'])
    assert available_markets == int(config['PAGE']['num_of_available_markets'])

    # verify that all filters are available
    geo_filter = page.get_by_role("button", name="Γεωγραφία")
    org_type_filter = page.get_by_role("button", name="Εταιρικός Τύπος")
    incorporation_date_filter = page.get_by_role("button", name="Μήνας Ίδρυσης")
    sales_filter = page.get_by_role("button", name="Πωλήσεις")

    assert geo_filter is not None
    assert org_type_filter is not None
    assert incorporation_date_filter is not None
    assert sales_filter is not None

    context.close()
    browser.close()
