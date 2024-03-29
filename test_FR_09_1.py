import configparser

from playwright.sync_api import Playwright, sync_playwright, expect


def test_case_id_9(playwright: Playwright) -> None:
    config = configparser.ConfigParser()
    config.read('config.env', 'utf-8')
    browser = playwright.chromium.launch(headless=False)
    # context = browser.new_context()
    context = browser.new_context(
        http_credentials={"username": config['HTTP CREDS']['username'],
                          "password": config['HTTP CREDS']['password']}
    )
    page = context.new_page()
    page.goto(config['PAGE']['Url'])

    # Successful Login
    page.get_by_role("button", name="Είσοδος/Εγγραφή").click()
    page.get_by_role("textbox", name="Email").fill(config['USER LOGIN']['email'])
    page.get_by_role("textbox", name="Password").fill(config['USER LOGIN']['password'])
    page.get_by_role("button", name="Είσοδος").click()

    # Go to user's profile basic info and ask
    page.get_by_text("B2B").click()
    page.get_by_role("button", name="Είσοδος στην Πλατφόρμα").click()
    page.locator("app-header").get_by_role("img").nth(3).click()
    page.get_by_role("button", name="Βασικές Πληροφορίες").click()
    page.get_by_role("button", name="Ανανέωση κωδικού").click()
    message = page.get_by_text("Έχει αποσταλεί email με οδηγιες για ανανέωση του κωδικού πρόσβασης.").nth(1)

    assert message is not None

    context.close()
    browser.close()
