import configparser

from playwright.sync_api import Playwright, Page, expect


def test_case_id_32(playwright: Playwright):
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

    page.get_by_text("B2B").click()
    page.get_by_role("button", name="Είσοδος στην Πλατφόρμα").click()

    page.get_by_role("button", name="Επιλογή Υπηρεσίας").click()
    page.get_by_role("button", name="B2B Dashboard").click(force=True)

    # click on first purchased lead
    page.get_by_text("Ξενοδοχεία" + " " + config['EXAMPLES']['b2bHotCnt_univ']).first.click()
    page.get_by_role("button", name="Προβολή σε Πίνακα").click()

    # Table columns headers
    first_column = page.get_by_role("columnheader", name="Επιχείρηση")
    second_column = page.get_by_role("columnheader", name="Αρ. ΓΕΜΗ")
    third_column = page.get_by_role("columnheader", name="Ίδρυση")
    fourth_column = page.get_by_role("columnheader", name="Κύρια Δραστηριότητα")
    fifth_column = page.get_by_role("columnheader", name="Διεύθυνση")

    assert first_column is not None
    assert second_column is not None
    assert third_column is not None
    assert fourth_column is not None
    assert fifth_column is not None

    context.close()
    browser.close()