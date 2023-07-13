import configparser

from playwright.sync_api import Playwright, Page, expect


def test_case_id_42(playwright: Playwright):
    config = configparser.ConfigParser()
    config.read('config.env', 'utf-8')
    browser = playwright.chromium.launch(headless=False)

    if "front" in config['PAGE']['Url']:
        context = browser.new_context(
            http_credentials={"username": config['PAGE']['http_creds_username'],
                              "password": config['PAGE']['http_creds_password']}
        )
    else:
        context = browser.new_context()

    page = context.new_page()
    page.goto(config['PAGE']['Url'])

    # Successful Login
    page.get_by_role("button", name="Είσοδος/Εγγραφή").click()
    page.get_by_role("textbox", name="Email").fill(config['USER LOGIN']['email'])
    page.get_by_role("textbox", name="Password").fill(config['USER LOGIN']['password'])
    page.get_by_role("button", name="Είσοδος").click()

    page.get_by_text("KYC (KNOW YOUR CUSTOMER)").click()
    page.get_by_role("button", name="Είσοδος στην Πλατφόρμα").click()

    page.get_by_placeholder("Αναζήτηση επιχείρησης με ΑΦΜ ή ΓΕΜΗ...").fill("800950289")
    page.get_by_placeholder("Αναζήτηση επιχείρησης με ΑΦΜ ή ΓΕΜΗ...").press("Enter")
    page.get_by_text("LB LINKED BUSINESS ΑΝΩΝΥΜΗ ΕΤΑΡΕΙΑ").click(force=True)
    basic_info = page.get_by_role("heading", name="Βασικά Στοιχεία").inner_text()
    bo = page.locator("app-company-overview").get_by_text("Διοίκηση & Ιδιοκτησία").inner_text()
    company_events = page.locator("app-company-overview").get_by_text("Εταιρικά Γεγονότα").inner_text()
    public_money = page.locator("app-company-overview").get_by_text("Δημόσιο Χρήμα").inner_text()

    assert basic_info == "Βασικά Στοιχεία"
    assert bo == "Διοίκηση & Ιδιοκτησία"
    assert company_events == "Εταιρικά Γεγονότα"
    assert public_money == "Δημόσιο Χρήμα"

    context.close()
    browser.close()
