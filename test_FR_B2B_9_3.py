import configparser

from playwright.sync_api import Playwright, sync_playwright, expect


def test_case_id_22(playwright: Playwright) -> None:
    config = configparser.ConfigParser()
    config.read('config.env', 'utf-8')
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(config['PAGE']['UrlB2B'])
    page.get_by_placeholder("Αναζήτηση Αγοράς...").click()
    page.get_by_role("option", name="Ξενοδοχεία" + " " + "(" + config['EXAMPLES']['b2bHotCnt_1'] + ")").click()
    page.get_by_role("button", name="Αναζήτηση").click()

    initial_market_value = page.locator(".stats-value").nth(0).inner_text().replace('.', '')

    page.get_by_role("button", name="Γεωγραφία").click()
    page.get_by_label("Περιφερειακή Ενότητα").check()
    page.get_by_placeholder("Όλες οι περιφερειακές ενότητες").click()
    page.get_by_role("button", name="Θεσσαλονίκης").click()
    page.get_by_text("Ακύρωση Εφαρμογή Φίλτρου").click()
    page.get_by_role("button", name="Αναζήτηση").click()

    filtered_market_value = page.locator(".stats-value").nth(0).inner_text().replace('.', '')

    assert initial_market_value > filtered_market_value

    context.close()
    browser.close()