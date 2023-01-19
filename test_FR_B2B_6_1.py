import configparser

from playwright.sync_api import Playwright, sync_playwright, expect


def test_case_id_16(playwright: Playwright) -> None:
    config = configparser.ConfigParser()
    config.read('config.env')
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(config['PAGE']['UrlB2B'])
    page.get_by_placeholder("Αναζήτηση Αγοράς...").click()
    page.get_by_role("option", name="Ξενοδοχεία (8.083)").click()
    page.get_by_role("button", name="Αναζήτηση").click()

    page.locator("[id=\"\\30 94027165\"]").get_by_text(
        "ΣΑΝΗ ΜΟΝΟΠΡΟΣΩΠΗ ΑΝΩΝΥΜΟΣ ΕΤΑΙΡΕΙΑ ΑΝΑΠΤΥΞΕΩΣ ΚΑΙ ΤΟΥΡΙΣΜΟΥ").click()
    name_on_map = page.get_by_role("heading", name="ΣΑΝΗ ΜΟΝΟΠΡΟΣΩΠΗ ΑΝΩΝΥΜΟΣ ΕΤΑΙΡΕΙΑ ΑΝΑΠΤΥΞΕΩΣ ΚΑΙ ΤΟΥΡΙΣΜΟΥ")

    assert name_on_map is not None

    context.close()
    browser.close()

