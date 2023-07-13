import configparser

from playwright.sync_api import Playwright, Page, expect

def test_case_id_44(playwright: Playwright):
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

    page.get_by_text("KYC (KNOW YOUR CUSTOMER)").click()
    page.get_by_role("button", name="Είσοδος στην Πλατφόρμα").click()

    page.get_by_placeholder("Αναζήτηση επιχείρησης με ΑΦΜ ή ΓΕΜΗ...").fill("800950289")
    page.get_by_placeholder("Αναζήτηση επιχείρησης με ΑΦΜ ή ΓΕΜΗ...").press("Enter")

    company_name = page.get_by_text("LB LINKED BUSINESS ΑΝΩΝΥΜΗ ΕΤΑΡΕΙΑ").inner_text()
    afm = page.get_by_text("ΑΦΜ").inner_text().split('|')[0].split(":")[1].strip()
    gemi = page.get_by_text("ΑΦΜ").inner_text().split('|')[1].split(":")[1].strip()
    address = page.get_by_text("ΠΑΤΡΙΑΡΧΟΥ").inner_text()
    main_activity =  page.get_by_text("Παροχή").inner_text()

    assert company_name == 'LB LINKED BUSINESS ΑΝΩΝΥΜΗ ΕΤΑΡΕΙΑ'
    assert afm == '800950289'
    assert gemi == '145587001000'
    assert address == 'ΠΑΤΡΙΑΡΧΟΥ ΓΡΗΓΟΡΙΟΥ Ε ΚΑΙ ΝΕΑ, ΠΑΤΡΙΑΡΧΟΥ ΓΡΗΓΟΡΙΟΥ Ε ΚΑΙ ΝΕΑ, ΑΓΙΑ ΠΑΡΑΣΚΕΥΗ'
    assert main_activity == 'Παροχή υπηρεσιών εφαρμογών πληροφορικής'

    # ---------------------
    context.close()
    browser.close()
