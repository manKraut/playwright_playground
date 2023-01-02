from playwright.sync_api import Playwright, Page, expect


def test_case_id_41(playwright: Playwright):
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
    page.get_by_placeholder("Αναζήτηση επιχείρησης με ΑΦΜ ή ΓΕΜΗ...").fill("094182927")
    page.get_by_role("button", name="Αναζήτηση").click()
    page.get_by_role("link", name="VETHELLAS ΑΕΒΕ ΚΤΗΝΙΑΤΡΙΚΩΝ ΧΗΜΙΚΩΝ ΚΓΕΩΡΓΙΚΩΝ ΕΦΟΔΙΩΝ").click()

    # check that results exists
    page.goto("https://app.linkedbusiness.eu/company/094182927/overview")

    # ---------------------
    context.close()
    browser.close()
