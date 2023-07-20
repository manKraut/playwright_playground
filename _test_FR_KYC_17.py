import configparser

from playwright.sync_api import Playwright, Page, expect
from datetime import datetime

def test_case_id_56(playwright: Playwright):
    config = configparser.ConfigParser()
    config.read('config.env', 'utf-8')
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(config['PAGE']['Url'])

    # Successful Login
    page.get_by_role("button", name="Είσοδος").click()
    page.get_by_placeholder("Email").click()
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill(config['USER']['Password'])
    page.get_by_placeholder("Email").click()
    page.get_by_placeholder("Email").fill(config['USER']['Email'])
    page.get_by_placeholder("Password").click()
    page.get_by_role("button", name="Είσοδος").click()

    #get date and create a name for the list

    current_dateTime = datetime.now()
    listName = "myList" + "_" + str(current_dateTime.year) + "_" + str(current_dateTime.month)  + "_"  +  str(current_dateTime.day)


    # list open
    page.locator("app-header").get_by_role("img").nth(3).click()
    page.get_by_role("link", name="Οι Λίστες Μου").click()
    page.get_by_role("heading", name=listName).click()
    page.get_by_role("row", name="Ημερομηνία Σύστασης Επωνυμία Διεύθυνση Κύρια Δραστηριότητα").get_by_role(
        "img").click()
    # find list data


    context.close()
    browser.close()