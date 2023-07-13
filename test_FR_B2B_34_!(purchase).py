import configparser

from playwright.sync_api import Playwright, sync_playwright, expect


def test_case_id_51(playwright: Playwright) -> None:
    config = configparser.ConfigParser()
    config.read('config.env', 'utf-8')
    browser = playwright.chromium.launch(headless=False)
    # context = browser.new_context()
    context = browser.new_context(
        http_credentials={"username": "lbUser", "password": "lbP4ss2022!"}
    )
    page = context.new_page()
    page.goto(config['PAGE']['Url'])

    # Successful Login
    page.get_by_role("button", name="Είσοδος/Εγγραφή").click()
    page.get_by_role("textbox", name="Email").fill(config['USER LOGIN']['email'])
    page.get_by_role("textbox", name="Password").fill(config['USER LOGIN']['password'])
    page.get_by_role("button", name="Είσοδος").click()

    page.get_by_text("B2B").click()
    page.get_by_role("button", name="Είσοδος στην Πλατφόρμα").click()

    # Choose market and add excel list to cart
    page.get_by_placeholder("Αναζήτηση Αγοράς...").click()
    page.get_by_role("option", name=config['EXAMPLES']['example_market']).click()
    page.get_by_role("button", name="Αναζήτηση").click()
    page.get_by_role("button", name="Λήψη Λίστας").click()
    page.get_by_role("button", name="Προσθήκη στο Καλάθι").click()

    # Proceed with payment
    page.locator("app-header").get_by_text("1").first.click()
    page.get_by_role("button", name="Checkout").click()
    page.get_by_role("button", name="Συνέχεια").click()
    page.get_by_placeholder("Εταιρικό ΑΦΜ").click()
    page.get_by_placeholder("Εταιρικό ΑΦΜ").fill("800950289")
    page.get_by_role("button", name="Συνέχεια").click()

    page.wait_for_timeout(3000)
    print("going to locate it")

    # page.on("frameattached", page.get_by_placeholder("Αριθμός κάρτας"))

    card_number_iframe = page.main_frame.child_frames[6].name
    print(card_number_iframe)
    page.frame_locator(card_number_iframe).get_by_role("presentation").click()
    page.frame_locator(card_number_iframe).get_by_role("presentation").fill("45444544454")
    # page.frame_locator(card_number_iframe).locator(".InputContainer").fill("45444544454")
    # page.frame_locator(f"#{card_number_iframe}").fill("434343434")


    # stripeFrame.wait_for_selector('input[name="Αριθμός κάρτας"]').fill('4242424242424242')
    # stripeFrame.locator('[placeholder="MM / YY"]').fill('04/30')
    # stripeFrame.locator('[placeholder="CVC"]').fill('242')


    context.close()
    browser.close()


