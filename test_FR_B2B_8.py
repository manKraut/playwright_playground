import configparser

from playwright.sync_api import Playwright, sync_playwright, expect


def test_case_id_22(playwright: Playwright) -> None:
    config = configparser.ConfigParser()
    config.read('config.env', 'utf-8')
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(
        http_credentials={"username": config['HTTP CREDS']['username'],
                          "password": config['HTTP CREDS']['password']}
    )
    page = context.new_page()
    page.goto(config['PAGE']['Url'])

    page.get_by_text("B2B").click()
    page.get_by_role("button", name="Είσοδος στην Πλατφόρμα").click()
    page.get_by_placeholder("Αναζήτηση Αγοράς...").click()
    page.get_by_role("option", name="Δεν βλέπετε την αγορά που σας ενδιαφέρει;Πατήστε εδώ...").click()
    title_on_page = page.get_by_role("heading", name="Όλες οι Αγορές")

    assert title_on_page is not None

    context.close()
    browser.close()
