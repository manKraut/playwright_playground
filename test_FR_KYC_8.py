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

    page.locator("app-money-block").get_by_role("button", name="Δείτε περισσότερα...").click()
    top_buyers = page.get_by_text("Μεγαλύτεροι Πληρωτές").inner_text()
    assignments = page.get_by_text("Αναθέσεις & Πληρωμές από το Δημόσιο").inner_text()
    payments_aggregations = page.get_by_text("Ποσό & Τύπος Απόφασης ανά Έτος").inner_text()

    assert top_buyers == "Μεγαλύτεροι Πληρωτές"
    assert assignments == "Αναθέσεις & Πληρωμές από το Δημόσιο"
    assert payments_aggregations == "Ποσό & Τύπος Απόφασης ανά Έτος"

    context.close()
    browser.close()