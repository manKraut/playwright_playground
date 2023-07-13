import configparser

from playwright.sync_api import Playwright, sync_playwright, expect


def test_case_id_43(playwright: Playwright) -> None:
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
    page.get_by_role("textbox", name="Email").fill(config['USER LOGIN']['email'])
    page.get_by_role("textbox", name="Password").fill(config['USER LOGIN']['password'])
    page.get_by_role("button", name="Είσοδος").click()

    page.get_by_text("B2B").click()
    page.get_by_role("button", name="Είσοδος στην Πλατφόρμα").click()

    # Go to dashboard and select first lead (Universe)
    page.get_by_role("button", name="Επιλογή Υπηρεσίας").click()
    page.get_by_role("button", name="B2B Dashboard").click(force=True)

    page.locator("div:nth-child(3) > .card-body-container").click()
    geo_filter_txt = page.get_by_role("button", name="Γεωγραφία").inner_text()
    org_type_filter_txt = page.get_by_role("button", name="Εταιρικός Τύπος").inner_text()
    inc_date_filter_txt = page.get_by_role("button", name="Μήνας Ίδρυσης").inner_text()
    sales_filter_txt = page.get_by_role("button", name="Πωλήσεις").inner_text()

    assert geo_filter_txt == "Γεωγραφία"
    assert org_type_filter_txt == "Εταιρικός Τύπος"
    assert inc_date_filter_txt == "Μήνας Ίδρυσης"
    assert sales_filter_txt == "Πωλήσεις"

    context.close()
    browser.close()
