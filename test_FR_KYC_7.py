import configparser

from playwright.sync_api import Playwright, Page, expect

def test_case_id_47(playwright: Playwright):
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
    page.get_by_role("link", name="Αξιολόγηση").click()


    #assume company is bought

    #look for labels

    page.get_by_text("Πιστοληπτική Διαβάθμιση").click()
    page.get_by_text("Κατάταξη στην Αγορά").click()
    page.get_by_role("tooltip", name="2021, 2020 ΠΙΣΤΩΤΙΚΟΣ ΚΙΝΔΥΝΟΣ ΥΨΗΛΟΣ").locator("img").click()
    page.get_by_role("tooltip", name="2021, 2020 ΑΝΟΔΙΚΗ").locator("img").click()

    context.close()
    browser.close()