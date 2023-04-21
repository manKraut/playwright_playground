import configparser

from playwright.sync_api import Playwright, sync_playwright, expect


def test_case_id_47(playwright: Playwright) -> None:
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


    # Go to B2B Sales Leads
    page.get_by_role("button", name="ΕΙΣΟΔΟΣ ΣΤΟ B2B").click()
    page.locator("app-button", has_text="Εταιρικός Τύπος").hover()
    page.wait_for_timeout(3000)
    cta = page.get_by_text(text='Το συγκεκριμένο φίλτρο', exact=False).all_text_contents()

    assert cta[0] == 'Το συγκεκριμένο φίλτρο είναι διαθέσιμο μόνο για registered χρήστες. Συνδεθείτε εάν έχετε ήδη λογαριασμό ή δημιουργήστε νέο δωρεάν.'

    context.close()
    browser.close()

