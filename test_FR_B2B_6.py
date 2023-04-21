import configparser

from playwright.sync_api import Playwright, sync_playwright, expect


def test_case_id_22(playwright: Playwright) -> None:
    config = configparser.ConfigParser()
    config.read('config.env', 'utf-8')
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    # context = browser.new_context(
    #     http_credentials={"username": "lbUser", "password": "lbP4ss2022!"}
    # )
    page = context.new_page()
    page.goto(config['PAGE']['Url'])

    page.get_by_text("B2B").click()
    page.get_by_role("button", name="Είσοδος στην Πλατφόρμα").click()

    page.get_by_placeholder("Αναζήτηση Αγοράς...").click()
    page.get_by_role("option", name=config['EXAMPLES']['example_market']).click()
    page.get_by_role("button", name="Αναζήτηση").click()

    page.get_by_role("region", name="Map").get_by_role("button").nth(2).click()
    name_on_map = page.get_by_role("heading", name="ΠΑΡΑΓΩΓΗ ΕΙΔΩΝ ΖΑΧΑΡΟΠΛΑΣΤΙΚΗΣ ΠΑΓΩΤΩΝ ΑΝΩΝΥΜΟΣ ΒΙΟΜΗΧΑΝΙΚΗ ΕΤΑΙΡΕΙΑ").inner_text()

    assert name_on_map == "ΠΑΡΑΓΩΓΗ ΕΙΔΩΝ ΖΑΧΑΡΟΠΛΑΣΤΙΚΗΣ ΠΑΓΩΤΩΝ ΑΝΩΝΥΜΟΣ ΒΙΟΜΗΧΑΝΙΚΗ ΕΤΑΙΡΕΙΑ"

    context.close()
    browser.close()
