import configparser

from playwright.sync_api import Playwright, Page, expect


def test_case_id_14(playwright: Playwright) -> None:
    config = configparser.ConfigParser()
    config.read('config.env', 'utf-8')
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(config['PAGE']['UrlB2B'])
    page.get_by_placeholder("Αναζήτηση Αγοράς...").click()
    page.get_by_role("option", name="Ξενοδοχεία (8.083)").click()
    page.get_by_role("button", name="Αναζήτηση").click()
    companies = page.locator(".stats-desc").nth(0).inner_text()
    last_month = page.locator(".stats-desc").nth(1).inner_text()
    three_months = page.locator(".stats-desc").nth(2).inner_text()
    year = page.locator(".stats-desc").nth(3).inner_text()

    assert companies == "Υφιστάμενες Επιχειρήσεις"
    assert last_month == "Ιδρύσεις (Νοεμβρίου)"
    assert three_months == "Ιδρύσεις Τριμήνου"
    assert year == "Ιδρύσεις Έτους"



    context.close()
    browser.close()



