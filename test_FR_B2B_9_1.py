import configparser

from playwright.sync_api import Playwright, sync_playwright, expect


def test_case_id_23(playwright: Playwright) -> None:
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


    page.get_by_text("B2B").click()
    page.get_by_role("button", name=config['PAGE']['entry_btn']).click()
    redirection_page = page.url




    #page.goto(config['PAGE']['UrlB2B'])
    page.get_by_placeholder("Αναζήτηση Αγοράς...").click()
    page.get_by_role("option", name="Ξενοδοχεία" + " " + "(" + config['EXAMPLES']['b2b_hotels_count_univ'] + ")").click()
    page.get_by_role("button", name="Αναζήτηση").click()

    initial_market_value = page.locator(".stats-value").nth(0).inner_text().replace('.', '')

    page.get_by_role("button", name="Γεωγραφία").click()
    page.get_by_placeholder("Όλα τα επιμελητήρια").click()
    page.get_by_role("button", name="Αθηνών Βιοτεχνικό").click()
    page.get_by_role("button", name="Εφαρμογή Φίλτρου").click()
    page.get_by_role("button", name="Αναζήτηση").click()

    filtered_market_value = page.locator(".stats-value").nth(0).inner_text().replace('.', '')

    assert initial_market_value > filtered_market_value

    context.close()
    browser.close()
