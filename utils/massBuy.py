from playwright.sync_api import Playwright, Page, expect


with open("test_comp.txt", 'r') as my_file:
    afms = []
    for line in my_file.readlines():
        afms.append(str.rstrip(line))

print(afms)


def test_buy_company(playwright: Playwright):


    # search afm-s and buy reports
    for afm in afms:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://app.linkedbusiness.eu/home")

        # Successful Login
        page.get_by_role("button", name="Είσοδος").click()
        page.get_by_placeholder("Email").click()
        page.get_by_placeholder("Email").fill("dimneg@gmail.com")
        page.get_by_placeholder("Password").click()
        page.get_by_placeholder("Password").fill("5CPM6OD2VfONebNDTHB8")
        page.get_by_role("button", name="Είσοδος").click()
        page.get_by_role("button", name="ΕΙΣΟΔΟΣ ΣΤΟ KYC").click()
        page.get_by_placeholder("Αναζήτηση επιχείρησης με ΑΦΜ ή ΓΕΜΗ...").click()
        page.get_by_placeholder("Αναζήτηση επιχείρησης με ΑΦΜ ή ΓΕΜΗ...").fill(afm)
        page.get_by_placeholder("Αναζήτηση επιχείρησης με ΑΦΜ ή ΓΕΜΗ...").press("Enter")
        page.locator(".card-title").click()
        page.get_by_role("button", name="Λήψη Report").click()
        page.locator("app-subscription-card").filter(
            has_text="ProΠρόσβαση στο LB Dashboard, με δυνατότητα δημιουργίας πολλαπλών watchlists, κα").get_by_role(
            "button", name="Εξαργύρωση").click()

