import configparser

from playwright.sync_api import Playwright, Page, expect


def test_case_id_10(playwright: Playwright):
    config = configparser.ConfigParser()
    config.read('config.env', 'utf-8')
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    # context = browser.new_context(
    #     http_credentials={"username": "lbUser", "password": "lbP4ss2022!"}
    # )
    page = context.new_page()
    page.goto(config['PAGE']['Url'])

    # Successful Login
    page.get_by_role("button", name="Είσοδος/Εγγραφή").click()
    page.get_by_role("textbox", name="Email").click()
    page.get_by_role("textbox", name="Email").fill(config['USER']['Email'])
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill(config['USER']['Password'])
    page.get_by_role("button", name="Είσοδος").click()

    # Access personal info
    page.get_by_text("B2B").click()
    page.get_by_role("button", name="Είσοδος στην Πλατφόρμα").click()
    page.locator("app-header").get_by_role("img").nth(3).click()
    page.get_by_role("button", name="Βασικές πληροφορίες").click()

    # Change personal info
    page.get_by_placeholder("Όνομα").click()
    page.get_by_placeholder("Όνομα").fill("MJ")
    page.get_by_placeholder("Επίθετο").click()
    page.get_by_placeholder("Επίθετο").fill("J")
    page.get_by_placeholder("Επωνυμία εταιρείας").click()
    page.get_by_placeholder("Επωνυμία εταιρείας").fill("MJ")
    page.get_by_placeholder("Τομέας Επαγγελματικής Δραστηριότητας").click()
    page.get_by_placeholder("Τομέας Επαγγελματικής Δραστηριότητας").fill("MJ")
    page.get_by_placeholder("Α.Φ.Μ.").click()
    page.get_by_placeholder("Α.Φ.Μ.").fill("800950289")
    page.get_by_placeholder("Οδός").click()
    page.get_by_placeholder("Οδός").fill("MJ")
    page.get_by_placeholder("Πόλη").click()
    page.get_by_placeholder("Πόλη").fill("MJ")
    page.get_by_placeholder("Νομός").click()
    page.get_by_placeholder("Νομός").fill("J")
    page.get_by_placeholder("Τ.Κ.").click()
    page.get_by_placeholder("Τ.Κ.").fill("11111")
    page.get_by_placeholder("Δ.Ο.Υ.").click()
    page.get_by_placeholder("Δ.Ο.Υ.").fill("M")
    page.get_by_placeholder("Τηλέφωνο").click()
    page.get_by_placeholder("Τηλέφωνο").fill("JJ")

    # Save Changes
    page.get_by_role("button", name="Αποθήκευση αλλαγών").click()

    context.close()
    browser.close()