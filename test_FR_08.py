import configparser

from playwright.sync_api import Playwright, Page, expect


def test_case_id_8(playwright: Playwright):
    config = configparser.ConfigParser()
    config.read('config.env', 'utf-8')
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(config['PAGE']['Url'])

    # Successful Login
    page.get_by_role("button", name="Είσοδος").click()
    page.get_by_placeholder("Email").click()
    page.get_by_placeholder("Email").fill(config['USER']['Email'])
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill(config['USER']['Password'])
    page.get_by_role("button", name="Είσοδος").click()

    # Access personal info
    page.locator("app-header").get_by_role("img").nth(3).click()
    page.get_by_role("button", name="Βασικές πληροφορίες").click()

    # Change personal info
    page.get_by_placeholder("'Ονομα").click()
    page.get_by_placeholder("'Ονομα").fill("MJ")
    page.get_by_placeholder("Επίθετο").click()
    page.get_by_placeholder("Επίθετο").fill("J")
    page.get_by_placeholder("Επωνυμία εταιρίας").click()
    page.get_by_placeholder("Επωνυμία εταιρίας").fill("MJ")
    page.get_by_placeholder("Δραστηριότητα εταιρίας").click()
    page.get_by_placeholder("Δραστηριότητα εταιρίας").fill("MJ")
    page.get_by_placeholder("Εταιρικό ΑΦΜ").click()
    page.get_by_placeholder("Εταιρικό ΑΦΜ").fill("MJ")
    page.get_by_placeholder("Διεύθυνση").click()
    page.get_by_placeholder("Διεύθυνση").fill("MJ")
    page.get_by_placeholder("Πόλη").click()
    page.get_by_placeholder("Πόλη").fill("MJ")
    page.get_by_placeholder("ΔΟΥ").click()
    page.get_by_placeholder("ΔΟΥ").fill("M")
    page.get_by_placeholder("Νομός").click()
    page.get_by_placeholder("Νομός").fill("J")
    page.get_by_placeholder("ΤΚ").click()
    page.get_by_placeholder("ΤΚ").fill("11111")
    page.get_by_placeholder("Νομός").click()
    page.get_by_placeholder("Νομός").fill("JJ")

    # Save Changes
    page.get_by_role("button", name="Αποθήκευση αλλαγών").click()
    page.get_by_role("link", name="Βασικές πληροφορίες").click()

    context.close()
    browser.close()