import configparser

from playwright.sync_api import Playwright, sync_playwright, expect


def test_case_id_15(playwright: Playwright) -> None:
    config = configparser.ConfigParser()
    config.read('config.env', 'utf-8')
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(config['PAGE']['UrlB2B'])
    page.get_by_placeholder("Αναζήτηση Αγοράς...").click()
    page.get_by_role("option", name="Ξενοδοχεία (8.083)").click()
    page.get_by_role("button", name="Αναζήτηση").click()

    # Result 1
    r1_name = page.get_by_text("ΣΑΝΗ ΜΟΝΟΠΡΟΣΩΠΗ ΑΝΩΝΥΜΟΣ ΕΤΑΙΡΕΙΑ ΑΝΑΠΤΥΞΕΩΣ ΚΑΙ ΤΟΥΡΙΣΜΟΥ")
    r1_afm_gemh_inDate = page.get_by_text("ΑΦΜ: 094027165 | ΓΕΜΗ: 121549104000 | Ίδρυση: Σεπτέμβριος 1968")
    r1_main_activity = page.locator("[id=\"\\30 94027165\"]").get_by_text("Κύρια Δραστηριότητα")
    r1_phone = page.locator("[id=\"\\30 94027165\"]").get_by_role("img").nth(2)
    r1_email = page.locator("[id=\"\\30 94027165\"]").get_by_role("img").nth(3)
    r1_website = page.locator("[id=\"\\30 94027165\"]").get_by_role("img").nth(4)

    assert r1_name is not None
    assert r1_afm_gemh_inDate is not None
    assert r1_main_activity is not None
    assert r1_phone is not None
    assert r1_email is not None
    assert r1_website is not None

    # Result 2
    r2_name = page.get_by_text("ΕΤΑΙΡΕΙΑ ΕΛΛΗΝΙΚΩΝ ΞΕΝΟΔΟΧΕΙΩΝ ΛΑΜΨΑ ΑΕ")
    r2_afm_gemh_inDate = page.get_by_text("ΑΦΜ: 094008519 | ΓΕΜΗ: 000223101000 | Ίδρυση: Δεκέμβριος 1919")
    r2_main_activity = page.locator("[id=\"\\30 94008519\"]").get_by_text("Κύρια Δραστηριότητα")
    r2_phone = page.locator("[id=\"\\30 94008519\"]").get_by_role("img").nth(2)
    r2_email = page.locator("[id=\"\\30 94008519\"]").get_by_role("img").nth(3)
    r2_website = page.locator("[id=\"\\30 94008519\"]").get_by_role("img").nth(4)

    assert r2_name is not None
    assert r2_afm_gemh_inDate is not None
    assert r2_main_activity is not None
    assert r2_phone is not None
    assert r2_email is not None
    assert r2_website is not None

    # Result 3
    r3_name = page.get_by_text("PRINCEISLANDS ΜΟΝΟΠΡΟΣΩΠΗ ΙΔΙΩΤΙΚΗ ΚΕΦΑΛΑΙΟΥΧΙΚΗ ΕΤΑΙΡΕΙΑ")
    r3_afm_gemh_inDate = page.get_by_text("ΑΦΜ: 801869891 | ΓΕΜΗ: 164890001000 | Ίδρυση: Ιούλιος 2022")
    r3_main_activity = page.locator("[id=\"\\38 01869891\"]").get_by_text("Κύρια Δραστηριότητα")
    r3_phone = page.locator("[id=\"\\38 01869891\"]").get_by_role("img").nth(2)
    r3_email = page.locator("[id=\"\\38 01869891\"]").get_by_role("img").nth(3)
    r3_website = page.locator("[id=\"\\38 01869891\"]").get_by_role("img").nth(4)

    assert r3_name is not None
    assert r3_afm_gemh_inDate is not None
    assert r3_main_activity is not None
    assert r3_phone is not None
    assert r3_email is not None
    assert r3_website is not None

    # Result 4
    r4_name = page.get_by_text("MILOS HOLDINGS ΙΔΙΩΤΙΚΗ ΚΕΦΑΛΑΙΟΥΧΙΚΗ ΕΤΑΙΡΕΙΑ")
    r4_afm_gemh_inDate = page.get_by_text("ΑΦΜ: 801924270 | ΓΕΜΗ: 166035903000 | Ίδρυση: Σεπτέμβριος 2022")
    r4_main_activity = page.locator("[id=\"\\38 01924270\"]").get_by_text("Κύρια Δραστηριότητα")
    r4_phone = page.locator("[id=\"\\38 01924270\"]").get_by_role("img").nth(2)
    r4_email = page.locator("[id=\"\\38 01924270\"]").get_by_role("img").nth(3)
    r4_website = page.locator("[id=\"\\38 01924270\"]").get_by_role("img").nth(4)

    assert r4_name is not None
    assert r4_afm_gemh_inDate is not None
    assert r4_main_activity is not None
    assert r4_phone is not None
    assert r4_email is not None
    assert r4_website is not None

    # Result 5
    r5_name = page.locator("[id=\"\\38 01852024\"]").get_by_text("MITOS SERVICES ΜΟΝΟΠΡΟΣΩΠΗ Ι Κ Ε")
    r5_afm_gemh_inDate = page.get_by_text("ΑΦΜ: 801852024 | ΓΕΜΗ: 164561103000 | Ίδρυση: Ιούνιος 2022")
    r5_main_activity = page.locator("[id=\"\\38 01852024\"]").get_by_text("Κύρια Δραστηριότητα")
    r5_phone = page.locator("[id=\"\\38 01852024\"]").get_by_role("img").nth(2)
    r5_email = page.locator("[id=\"\\38 01852024\"]").get_by_role("img").nth(3)
    r5_website = page.locator("[id=\"\\38 01852024\"]").get_by_role("img").nth(4)

    assert r5_name is not None
    assert r5_afm_gemh_inDate is not None
    assert r5_main_activity is not None
    assert r5_phone is not None
    assert r5_email is not None
    assert r5_website is not None

    context.close()
    browser.close()