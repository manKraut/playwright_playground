import configparser

from playwright.sync_api import Playwright, Page, expect

def test_case_id_52(playwright: Playwright):
    config = configparser.ConfigParser()
    config.read('config.env', 'utf-8')
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(config['PAGE']['Url'])

    # Successful Login
    page.get_by_role("button", name="Είσοδος").click()
    page.get_by_placeholder("Email").click()
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill(config['USER']['Password'])
    page.get_by_placeholder("Email").click()
    page.get_by_placeholder("Email").fill(config['USER']['Email'])
    page.get_by_placeholder("Password").click()
    page.get_by_role("button", name="Είσοδος").click()
    page.get_by_role("button", name="ΕΙΣΟΔΟΣ ΣΤΟ KYC").click()

    # Successful Login
    page.get_by_placeholder("Αναζήτηση επιχείρησης με ΑΦΜ ή ΓΕΜΗ...").fill(config['EXAMPLES']['g1']) #company gemh
    page.get_by_role("button", name="Αναζήτηση").click()
    page.get_by_role("link", name=config['EXAMPLES']['cn1']).click() #company name
    page.get_by_role("link", name="Δυσμενή Γεγονότα").click()


    #assume company is bought

    #look for labels

    page.get_by_text("Συναλλακτική Συμπεριφορά").click()
    page.get_by_text("Μέσος Δείκτης 4-ετίας").click()
    page.get_by_text(config['EXAMPLES']['dg11'])
    page.get_by_text(config['EXAMPLES']['dg12'])


    context.close()
    browser.close()