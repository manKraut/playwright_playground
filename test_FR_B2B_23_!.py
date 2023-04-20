import configparser


from playwright.sync_api import Playwright, sync_playwright, expect


def test_case_id_38(playwright: Playwright) -> None:
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
    page.get_by_role("textbox", name="Email").click()
    page.get_by_role("textbox", name="Email").fill(config['USER']['Email'])
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill(config['USER']['Password'])
    page.get_by_role("button", name="Είσοδος").click()

    page.get_by_text("B2B").click()
    page.get_by_role("button", name=config['PAGE']['entry_btn']).click()
    redirection_page = page.url

    #
    #page.get_by_role("button", name="ΕΙΣΟΔΟΣ ΣΤΟ B2B").click()
    page.get_by_placeholder("Αναζήτηση Αγοράς...").click()
    page.get_by_role("option", name=f"Ξενοδοχεία ({config['EXAMPLES']['b2b_hotels_count_univ']})").click()
    page.get_by_role("button", name="Αναζήτηση").click()
    page.get_by_role("button", name="Λήψη Λίστας").click()
    page.get_by_role("button", name="Προσθήκη στο Καλάθι").click()
    page.locator(".notification-number").first.click()
    page.get_by_role("button", name="Checkout").click()
    page.get_by_role("button", name="Συνέχεια").click()

    page.timeout(120000)

    context.close()
    browser.close()