import configparser

from playwright.sync_api import Playwright, Page, expect

def test_case_id_45(playwright: Playwright):
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
    page.get_by_role("link", name="Επιδόσεις").click()


    #assume company is bought

    #look for labers
    # Πωλήσεις & Κέρδη
    # €3,2M, €110,15K

    page.get_by_text("Πωλήσεις").click()
    page.get_by_text("Κέρδη").first.click()
    page.get_by_text(config['EXAMPLES']['fr1']).click()
    page.get_by_text(config['EXAMPLES']['fr2']).click()

    context.close()
    browser.close()