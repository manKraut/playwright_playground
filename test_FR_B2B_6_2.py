import configparser

from playwright.sync_api import Playwright, sync_playwright, expect


def test_case_id_17(playwright: Playwright) -> None:
    config = configparser.ConfigParser()
    config.read('config.env', 'utf-8')
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(config['PAGE']['UrlB2B'])
    page.get_by_placeholder("Αναζήτηση Αγοράς...").click()
    page.get_by_role("option", name="Ξενοδοχεία" + " " + "(" + config['EXAMPLES']['b2bHotCnt_1'] + ")").click()
    page.get_by_role("button", name="Αναζήτηση").click()

    page.get_by_text(config['EXAMPLES']['cn4']).click()
    name_on_map = page.get_by_role("heading", name=config['EXAMPLES']['cn4'])

    assert name_on_map is not None

    context.close()
    browser.close()