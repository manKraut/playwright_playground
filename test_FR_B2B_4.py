import configparser

from playwright.sync_api import Playwright, Page, expect


def test_case_id_20(playwright: Playwright) -> None:
    config = configparser.ConfigParser()
    config.read('config.env', 'utf-8')
    browser = playwright.chromium.launch(headless=False)
    # context = browser.new_context()
    context = browser.new_context(
        http_credentials={"username": "lbUser", "password": "lbP4ss2022!"}
    )
    page = context.new_page()
    page.goto(config['PAGE']['Url'])

    page.get_by_text("B2B").click()
    page.get_by_role("button", name="Είσοδος στην Πλατφόρμα").click()

    page.get_by_placeholder("Αναζήτηση Αγοράς...").click()
    page.get_by_role("option", name=config['EXAMPLES']['example_market']).click()
    page.get_by_role("button", name="Αναζήτηση").click()


    stats_area = page.locator("div.stats-content").nth(0)
    companies = stats_area.locator("div.companies-count").nth(0).nth(0).inner_text().split("\n")[1]
    establishments = stats_area.locator("div.companies-establishments").nth(0).nth(0).inner_text()
    last_month = establishments.split('\n')[1]
    three_months = establishments.split('\n')[3]
    year = establishments.split('\n')[5]

    assert companies == "Υφιστάμενες Επιχειρήσεις"
    assert last_month == "Ιδρύσεις (Μαρτίου)"
    assert three_months == "Ιδρύσεις Τριμήνου"
    assert year == "Ιδρύσεις Έτους"

    context.close()
    browser.close()
