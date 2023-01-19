from playwright.sync_api import Playwright, sync_playwright, expect


def test_case_id_33(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://app.linkedbusiness.eu/home")

    # Successful Login
    page.get_by_role("button", name="Είσοδος").click()
    page.get_by_placeholder("Email").click()
    page.get_by_placeholder("Email").fill("m.adamopoulos@lbsuite.eu")
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("Test123!")
    page.get_by_role("button", name="Είσοδος").click()

    # Search for a arket, erase the selected market from search bar
    page.goto("https://app.linkedbusiness.eu/b2b-dashboard")
    page.get_by_role("option", name="Ξενοδοχεία (8.083)").click()
    page.get_by_role("button", name="Αναζήτηση").click()
    page.get_by_placeholder("Αναζήτηση Αγοράς...").click()
    page.get_by_text("Εργαλείο Διαστασιολόγησης ΑγορώνΞενοδοχεία (8.083)Δεν βλέπετε την αγορά που σας ").click()
    page.get_by_placeholder("Αναζήτηση Αγοράς...").click()
    page.get_by_placeholder("Αναζήτηση Αγοράς...").fill("")
    dropdown_nemu = page.get_by_text("Κομμωτήρια (11.828)Ξενοδοχεία (8.083)Supermarkets, Παντοπωλεία & Περίπτερα (16.5").click()

    #verify that the dropdown menu with all markets is still available
    assert dropdown_nemu is not None

    context.close()
    browser.close()