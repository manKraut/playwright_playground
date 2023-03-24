import configparser

from playwright.sync_api import Playwright, sync_playwright, expect


def test_case_id_46(playwright: Playwright) -> None:
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

    # Go to B2B Sales Leads and select market "Ξενοδοχεία"
    page.get_by_role("button", name="ΕΙΣΟΔΟΣ ΣΤΟ B2B").click()
    page.get_by_placeholder("Αναζήτηση Αγοράς...").click()
    page.get_by_role("option", name="Ξενοδοχεία (8.280)").click()
    page.get_by_role("button", name="Αναζήτηση").click()

    # Press the button "Δείτε τις υπόλοιπες Χ"
    page.get_by_role("button", name=f"Αποκτήστε τις υπόλοιπες {config['EXAMPLES']['b2b_hotels_count_univ']}").click()
    url = page.url

    assert url is "https://app.linkedbusiness.eu/b2b-dashboard/b2b-my-leads?subscriptionId=119"

    context.close()
    browser.close()
