import configparser

from playwright.sync_api import Playwright, sync_playwright, expect


def test_case_id_18(playwright: Playwright) -> None:
    config = configparser.ConfigParser()
    config.read('config.env')
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(config['PAGE']['UrlB2B'])
    page.get_by_placeholder("Αναζήτηση Αγοράς...").click()
    page.get_by_role("option", name="Ξενοδοχεία (8.083)").click()
    page.get_by_role("button", name="Αναζήτηση").click()

    page.locator("[id=\"\\30 94027165\"]").get_by_role("button", name="Εταιρικό Report").click()
    page.wait_for_timeout(3000) # set timeout to wait for the real url before assertion
    redirection_url = page.url

    assert redirection_url == "https://app.linkedbusiness.eu/company/094027165/overview"

    context.close()
    browser.close()