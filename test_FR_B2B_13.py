import configparser

from playwright.sync_api import Playwright, Page, expect


def test_case_id_29(playwright: Playwright):
    config = configparser.ConfigParser()
    config.read('config.env', 'utf-8')
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(config['PAGE']['Url'])

    # Successful Login
    page.get_by_role("button", name="Είσοδος").click()
    page.get_by_placeholder("Email").click()
    page.get_by_placeholder("Email").fill(config['USER']['Email'])
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill(config['USER']['Password'])
    page.get_by_role("button", name="Είσοδος").click()

    page.get_by_role("button", name="ΕΙΣΟΔΟΣ ΣΤΟ B2B").click()

    page.get_by_role("link", name="B2B Dashboard").click()
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
