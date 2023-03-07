import configparser

from playwright.sync_api import Playwright, sync_playwright, expect


def test_case_id_32(playwright: Playwright) -> None:
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

    page.get_by_role("button", name="ΕΙΣΟΔΟΣ ΣΤΟ B2B").click()
    page.get_by_placeholder("Αναζήτηση Αγοράς...").click()
    page.get_by_role("option", name="Ξενοδοχεία" + " " + "(" + config['EXAMPLES']['b2bHotCnt_1'] + ")").click()
    page.get_by_role("button", name="Αναζήτηση").click()

    # Purchase a Live package
    page.get_by_role("button", name="Λήψη Λίστας").click()
    page.get_by_role("button", name="Συνέχεια").click()
    page.locator("app-subscription-card").filter(has_text="HOTELS LiveΘέλετε να φτάνετε πρώτοι στους δυνητικούς σας πελάτες; Η Linked Busin").get_by_role("button", name="Προσθήκη στο Καλάθι").click()
    page.get_by_role("button", name="Close").nth(1).click()
    page.locator("app-header").get_by_text("1").first.click()
    page.get_by_role("button", name="Checkout").click()
    page.get_by_role("button", name="Συνέχεια").click()

    page.locator(".card-item").first.click()
    page.get_by_placeholder("Αριθμός κάρτας").fill(
        "4242 4242 4242 42422")
    page.frame_locator("iframe[name=\"__privateStripeFrame4496\"]").get_by_placeholder("Αριθμός κάρτας").press("Tab")
    page.frame_locator("iframe[name=\"__privateStripeFrame4497\"]").get_by_placeholder("MM/YY").fill("03 / 26")
    page.frame_locator("iframe[name=\"__privateStripeFrame4497\"]").get_by_placeholder("MM/YY").press("Tab")
    page.frame_locator("iframe[name=\"__privateStripeFrame4498\"]").get_by_placeholder("CVV").fill("123")
    page.get_by_role("button", name="Συνέχεια").click()

    # page.locator('').get_by_text("Αριθμός κάρτας").fill("4242 4242 4242 4242")
    # page.get_by_placeholder("Αριθμός κάρτας").fill("4 242 4242 4242 4242")
    # page.get_by_placeholder("MM/YY").click()
    # page.get_by_placeholder("MM/YY").fill("01 / 25")
    # page.get_by_placeholder("CVV").click()
    # page.get_by_placeholder("CVV").fill("333")
    # page.get_by_role("button", name="Συνέχεια").click()
    # page.get_by_role("button", name="Πληρωμή και Λήψη").click()
    # notification_for_purchase = page.get_by_text("Ευχαριστούμε για την εμπιστοσύνη σας στην πλατφόρμα έξυπνης επιχειρηματικής πληρ").nth(1)

    # assert notification_for_purchase is not None

    context.close()
    browser.close()