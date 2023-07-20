import configparser

from playwright.sync_api import Playwright, Page, expect

def test_case_id_55(playwright: Playwright):
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

    # Enter AFM and visit company's KYC Profile
    page.get_by_placeholder("Αναζήτηση επιχείρησης με ΑΦΜ ή ΓΕΜΗ...").fill(config['EXAMPLES']['kyc_vat'])
    page.get_by_placeholder("Αναζήτηση επιχείρησης με ΑΦΜ ή ΓΕΜΗ...").press("Enter")
    page.get_by_text("LB LINKED BUSINESS ΑΝΩΝΥΜΗ ΕΤΑΡΕΙΑ").click(force=True)

    # go to my lists
    page.locator("app-header").get_by_role("img").nth(4).click()
    page.get_by_role("button", name="Οι Λίστες Μου").click()
    page.get_by_role("heading", name="my_list").click()
    # verify the extract button exists
    extract_button = page.get_by_role("button", name="Εξαγωγή").inner_text()

    assert extract_button == "Εξαγωγή"

    context.close()
    browser.close()
