import configparser
import time

from playwright.sync_api import Playwright, sync_playwright, expect


def test_case_id_12(playwright: Playwright) -> None:
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

    # Create a unique username and password
    username = str(int(time.time())) + "@gmail.com"
    password = str(int(time.time())) + "Test123!"

    # Login as a new user
    page.get_by_role("button", name="Είσοδος/Εγγραφή").click()
    page.get_by_role("button", name="Εγγραφή νέου χρήστη").click()
    page.get_by_placeholder("Ονοματεπώνυμο").fill("Fake Fakopoulos")
    page.get_by_role("textbox", name="Email").fill(username)
    page.locator("#reg-password").fill(password)
    page.get_by_placeholder("Επιβεβαίωση password").fill(password)
    page.get_by_role("button", name="Εγγραφή").click()
    page.get_by_role("button", name="Εντάξει").click()
    page.wait_for_timeout(3000)
    redirection_url = page.url

    assert redirection_url == "https://front.linkedbusiness.eu/"

    context.close()
    browser.close()
