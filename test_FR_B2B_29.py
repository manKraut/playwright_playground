import configparser

from playwright.sync_api import Playwright, sync_playwright, expect


def test_case_id_43(playwright: Playwright) -> None:
    config = configparser.ConfigParser()
    config.read('config.env', 'utf-8')
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(config['PAGE']['Url'])

    # Successful Login
    page.get_by_role("button", name="Είσοδος").click()
    page.get_by_placeholder("Email").click()
    page.get_by_placeholder("Email").fill(config['USER']['Email'])
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill(config['USER']['Password'])
    page.get_by_role("button", name="Είσοδος").click()

    # Go to dashboard and select specific lead "Ξενοδοχεία"
    page.get_by_role("button", name="ΕΙΣΟΔΟΣ ΣΤΟ B2B").click()
    page.get_by_role("link", name="B2B Dashboard").click()
    page.get_by_text("Ξενοδοχεία 116 Ίδρυση έως Μάρτιος 2023 Περιφέρεια Αττικής, Κρήτης"
                     " Τύπος ΑΕ, ΕΠΕ, ΙΚΕ Πωλήσεις (€) 2M-10M").click()

    # Collect available filters options
    page.get_by_role("button", name="Γεωγραφία").click()
    page.get_by_placeholder("Όλες οι περιφέρειες").click()
    regions = [page.get_by_role("button", name="Αττικής"),
               page.get_by_role("button", name="Κρήτης")]
    page.get_by_role("img").first.click()

    page.get_by_role("button", name="Εταιρικός Τύπος").click()
    org_types = [page.get_by_role("group", name="Radio type").get_by_text("ΑΕ"),
                 page.get_by_role("group", name="Radio type").get_by_text("ΙΚΕ"),
                 page.get_by_role("group", name="Radio type").get_by_text("ΕΠΕ")]
    page.get_by_role("img").first.click()

    page.get_by_role("button", name="Πωλήσεις").click()
    sales_range = page.get_by_label("2M - 10M")
    page.get_by_role("img").first.click()

    assert len(regions) > 1
    assert len(org_types) > 1
    assert sales_range is not None

    context.close()
    browser.close()
