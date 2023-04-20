import configparser

from playwright.sync_api import Playwright, Page, expect


def test_case_id_11(playwright: Playwright):
    config = configparser.ConfigParser()
    config.read('config.env', 'utf-8')
    browser = playwright.chromium.launch(headless=False)
    # context = browser.new_context()
    context = browser.new_context(
        http_credentials={"username": "lbUser", "password": "lbP4ss2022!"}
    )
    page = context.new_page()
    page.goto(config['PAGE']['Url'])

    # Successful Login
    page.get_by_role("button", name="Είσοδος/Εγγραφή").click()
    page.get_by_role("textbox", name="Email").click()
    page.get_by_role("textbox", name="Email").fill(config['USER']['Email'])
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill(config['USER']['Password'])
    page.get_by_role("button", name="Είσοδος").click()

    # Purchase a list and verify that a warning for blank left field is shown
    page.get_by_text("B2B").click()
    page.get_by_role("button", name="Είσοδος στην Πλατφόρμα").click()
    page.get_by_placeholder("Αναζήτηση Αγοράς...").click()
    page.get_by_role("option", name=config['EXAMPLES']['example_market']).click()
    page.get_by_role("button", name="Αναζήτηση").click()
    page.get_by_role("button", name="Λήψη Λίστας").click()
    page.get_by_role("button", name="Προσθήκη στο Καλάθι").click()

    # page.get_by_role("img").nth(1).click()  Must be fulfiled with iframe which is under investigation

    page.get_by_role("button", name="Checkout").click()
    page.get_by_role("button", name="Συνέχεια").click()
    page.get_by_placeholder("Διεύθυνση").click()
    page.get_by_placeholder("Διεύθυνση").fill("")
    page.get_by_placeholder("Τηλέφωνο").click()
    warning_text = page.get_by_text("Το πεδίο ειναι υποχρεωτικό.").click()

    assert warning_text is not None

    context.close()
    browser.close()
