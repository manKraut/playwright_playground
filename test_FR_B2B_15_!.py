import configparser

from playwright.sync_api import Playwright, Page, expect


def test_case_id_31(playwright: Playwright):
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
    page.locator("app-b2b-markets-view").get_by_role("img").nth(1).click()
    # click at a point on map
    page.locator("div:nth-child(3) > div:nth-child(4)").click()
    # get the name of the company, showing on the map
    name_on_map = page.get_by_role("heading", name=config['EXAMPLES']['cn5'] )

    assert name_on_map is not None

    context.close()
    browser.close()