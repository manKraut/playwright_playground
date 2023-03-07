import configparser


from playwright.sync_api import Playwright, sync_playwright, expect


def test_case_id_33(playwright: Playwright) -> None:
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

    # Navigate through profile icon to the purchase list
    page.locator("app-header").get_by_role("img").nth(4).click()
    page.get_by_role("button", name="Ιστορικό Αγορών").click()
    expect(page).to_have_url(config['PAGE']['UrlS'] + "/" + "user-profile" + "/" + "buy-history")

    context.close()
    browser.close()