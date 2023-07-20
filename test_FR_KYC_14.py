import configparser

from playwright.sync_api import Playwright, Page, expect
from datetime import datetime

def test_case_id_54(playwright: Playwright):
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

    # get date and create a name for the list
    current_date_time = datetime.now()
    list_name = "myList" + "_" + str(current_date_time.year) + "_" + str(current_date_time.month) + "_" + str(
        current_date_time.day)

    # create new list from inside the profile, and add it to the list
    page.get_by_role("button", name="Προσθήκη σε Λίστα").click(force=True)
    page.get_by_text("Προσθήκη σε Νέα Λίστα").click()
    # page.get_by_role("button", name="Προσθήκη σε Νέα Λίστα").click(force=True)
    page.get_by_placeholder("Όνομα λίστας").fill(list_name)
    page.get_by_role("button", name="Δημιουργία Λίστας").click()
    into_one_list_button = page.get_by_role("button", name="Σε 1 λίστα").inner_text()

    assert into_one_list_button is not None

    # create new list through profile icon
    page.locator("app-header").get_by_role("img").nth(4).click()
    page.get_by_role("button", name="Οι Λίστες Μου").click()
    page.get_by_text("Δημιουργία Νέας Λίστας").click()
    page.get_by_placeholder("Όνομα λίστας").click()
    page.get_by_placeholder("Όνομα λίστας").fill(list_name)
    page.get_by_role("button", name="Δημιουργία Λίστας").click()
    list_in_my_lists = page.get_by_role("heading", name=list_name).inner_text()

    assert list_in_my_lists == list_name

    context.close()
    browser.close()