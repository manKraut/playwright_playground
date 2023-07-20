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
    page.wait_for_timeout(2000)

    # Go to notifications and search for a received alert for company events
    page.locator("app-header").get_by_role("img").nth(3).click()
    page.get_by_role("link", name="Δείτε περισσότερα...").click()
    page.get_by_placeholder("Αναζήτηση στις ειδοποιήσεις...").fill("εταιρικά")
    alert_string_list = page.get_by_role("heading", name="Εταιρικά Γεγονότα\nGRENZEBACH HELLAS ΜΟΝΟΠΡΟΣΩΠΗ ΑΝΩΝΥΜΗ ΕΤΑΙΡΕΙΑ")\
        .click()
    page.get_by_role("button", name="Μετάβαση στα Στοιχεία").click()
    page.wait_for_timeout(4000)
    redirect_link = page.url

    assert redirect_link == "https://front.linkedbusiness.eu/company/094543436/corporate-events"

    context.close()
    browser.close()
