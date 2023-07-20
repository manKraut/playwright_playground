import configparser

from playwright.sync_api import Playwright, Page, expect

def test_case_id_53(playwright: Playwright):
    config = configparser.ConfigParser()
    config.read('config.env', 'utf-8')
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(config['PAGE']['Url'])

    # Successful Login
    page.get_by_role("button", name="Είσοδος").click()
    page.get_by_placeholder("Email").click()
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill(config['USER']['Password'])
    page.get_by_placeholder("Email").click()
    page.get_by_placeholder("Email").fill(config['USER']['Email'])
    page.get_by_placeholder("Password").click()
    page.get_by_role("button", name="Είσοδος").click()

    # Access purchase history
    page.locator("app-header").get_by_role("img").nth(3).click()
    page.get_by_role("button", name="Ιστορικό Αγορών").click()
    with page.expect_download() as download_info:
        page.get_by_role("row", name="21/02/2023 Εταιρικό Report (PDF), ΠΙΕΡΙΚΗ ΧΟΙΡΕΙΟΥ ΚΡΕΑΤΟΣ ΑΕ").get_by_role("img").nth(1).click()
    download = download_info.value




    context.close()
    browser.close()