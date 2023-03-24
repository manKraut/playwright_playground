import configparser

from playwright.sync_api import Playwright, sync_playwright, expect


def test_case_id_9(playwright: Playwright) -> None:
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

    # Go to user's profile basic info and ask
    page.locator("app-header").get_by_role("img").nth(4).click()
    page.get_by_role("button", name="Βασικές Πληροφορίες").click()
    page.get_by_role("button", name="Ανανέωση κωδικού").click()
    message = page.get_by_text("Έχει αποσταλεί email με οδηγιες για ανανέωση του κωδικού πρόσβασης.").nth(1)

    assert message == "Έχει αποσταλεί email με οδηγιες για ανανέωση του κωδικού πρόσβασης."

    context.close()
    browser.close()
