#import configparser


from playwright.sync_api import Playwright, Page, expect


def test_case_id_43(playwright: Playwright):
    #config = configparser.ConfigParser()
    #config.read('config.env')
    #print config.get('USER','Email')
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://app.linkedbusiness.eu/home")
    # Successful Login
    page.get_by_role("button", name="Είσοδος").click()
    page.get_by_placeholder("Email").click()
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("OJuWboG0VE5foj1czGen")
    page.get_by_placeholder("Email").click()
    page.get_by_placeholder("Email").fill("d.negkas@lbsuite.eu")
    page.get_by_placeholder("Password").click()
    page.get_by_role("button", name="Είσοδος").click()
    page.get_by_role("button", name="ΕΙΣΟΔΟΣ ΣΤΟ KYC").click()

    # Verify that the user is able to search for companies using VAT ID
    page.get_by_placeholder("Αναζήτηση επιχείρησης με ΑΦΜ ή ΓΕΜΗ...").click()
    page.get_by_placeholder("Αναζήτηση επιχείρησης με ΑΦΜ ή ΓΕΜΗ...").fill("053108548000")
    page.get_by_role("button", name="Αναζήτηση").click()
    page.get_by_role("link", name="ΠΙΕΡΙΚΗ ΧΟΙΡΕΙΟΥ ΚΡΕΑΤΟΣ ΑΝΩΝΥΜΗ ΕΤΑΙΡΙΑ").click()

    # check that results exists
    page.goto("https://app.linkedbusiness.eu/company/094182927/overview")

    # ---------------------
    context.close()
    browser.close()
