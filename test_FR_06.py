import configparser

from playwright.sync_api import Playwright, Page, expect


def test_case_id_6(playwright: Playwright):
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

    # Successful Login
    page.get_by_role("button", name="Είσοδος/Εγγραφή").click()
    page.get_by_role("textbox", name="Email").fill(config['USER LOGIN']['email'])
    page.get_by_role("textbox", name="Password").fill(config['USER LOGIN']['password'])
    page.get_by_role("button", name="Είσοδος").click()

    # Access personal info
    page.get_by_text("B2B").click()
    page.get_by_role("button", name="Είσοδος στην Πλατφόρμα").click()
    page.locator("app-header").get_by_role("img").nth(3).click()
    page.get_by_role("button", name="Βασικές πληροφορίες").click()

    info_text = ["Όνομα", "Επίθετο", "Στοιχεία Λογαριασμού", "Στοιχεία Χρέωσης", "Επωνυμία εταιρείας",
                  "Τομέας Επαγγελματικής Δραστηριότητας", "Α.Φ.Μ.", "Οδός", "Πόλη", "Δ.Ο.Υ.", "Τ.Κ.", "Νομός"]

    for info in info_text:
        assert page.get_by_text(info).inner_text() == info


    context.close()
    browser.close()
