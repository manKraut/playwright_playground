import configparser

from playwright.sync_api import Playwright, Page, expect

def test_case_id_44(playwright: Playwright):
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

    # Verify that the user is able to see company's info (basic) and all the potential data blocks (header free mode)
    page.get_by_placeholder("Αναζήτηση επιχείρησης με ΑΦΜ ή ΓΕΜΗ...").fill(config['EXAMPLES']['g1'])
    page.get_by_role("button", name="Αναζήτηση").click()
    page.get_by_role("link", name=config['EXAMPLES']['cn1']).click() #company name 1
    page.goto(config['PAGE']['UrlKYCl'] + "/" + config['EXAMPLES']['v1'] + "/" + "overview") #company VAT

    # check that results exists .....

    page.goto(config['PAGE']['UrlKYCl'] + "/" + config['EXAMPLES']['v1'] + "/" + "overview")

    # ---------------------
    context.close()
    browser.close()