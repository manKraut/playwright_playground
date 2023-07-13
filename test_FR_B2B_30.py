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
    page.get_by_role("textbox", name="Email").fill(config['USER LOGIN']['email'])
    page.get_by_role("textbox", name="Password").fill(config['USER LOGIN']['password'])
    page.get_by_role("button", name="Είσοδος").click()

    page.get_by_text("B2B").click()
    page.get_by_role("button", name="Είσοδος στην Πλατφόρμα").click()

    # Go to dashboard and select specific lead
    page.get_by_role("button", name="Επιλογή Υπηρεσίας").click()
    page.get_by_role("button", name="B2B Dashboard").click(force=True)

    page.locator("div:nth-child(3) > .card-body-container").click()

    # Verify the sorting filters are available
    page.get_by_role("button", name="Ταξινόμηση κατά").click()
    inc_date_sorting_filter = page.get_by_role("button", name="Ημερομηνία").first.inner_text().strip()
    org_type_sorting_filter = page.get_by_role("button", name="Εταιρικός Τύπος").first.inner_text().strip()
    sales_sorting_filter = page.get_by_role("button", name="Πωλήσεις").first.inner_text().strip()

    assert inc_date_sorting_filter == "Ημερομηνία"
    assert org_type_sorting_filter == "Εταιρικός Τύπος"
    assert sales_sorting_filter == "Πωλήσεις"

    context.close()
    browser.close()
