import configparser

from playwright.sync_api import Playwright, Page, expect


def test_case_id_20(playwright: Playwright) -> None:
    config = configparser.ConfigParser()
    config.read('config.env', 'utf-8')
    browser = playwright.chromium.launch(headless=False)
    # context = browser.new_context()
    context = browser.new_context(
        http_credentials={"username": config['HTTP CREDS']['username'],
                          "password": config['HTTP CREDS']['password']}
    )
    page = context.new_page()
    page.goto(config['PAGE']['Url'])

    page.get_by_text("B2B").click()
    page.get_by_role("button", name="Είσοδος στην Πλατφόρμα").click()

    page.get_by_placeholder("Αναζήτηση Αγοράς...").click()
    page.get_by_role("option", name=config['EXAMPLES']['example_market']).click()

    # companies = page.get_by_text("Υφιστάμενες Επιχειρήσεις")


    stats_area = page.locator("div.stats-content").nth(0)
    companies = stats_area.locator("div.companies-count").nth(0).nth(0).inner_text().split("\n")[0]
    establishments = stats_area.locator("div.companies-establishments").nth(0).nth(0).inner_text()
    last_month = establishments.split('\n')[0].split()[0]
    three_months = establishments.split('\n')[2]
    year = establishments.split('\n')[4]

    assert companies == "Υφιστάμενες Επιχειρήσεις"
    assert last_month == "Ιδρύσεις"
    assert three_months == "Ιδρύσεις Τριμήνου"
    assert year == "Ιδρύσεις Έτους"

    context.close()
    browser.close()
