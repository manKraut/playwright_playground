import configparser

from playwright.sync_api import Playwright, sync_playwright, expect


def test_case_id_21(playwright: Playwright) -> None:
    config = configparser.ConfigParser()
    config.read('config.env', 'utf-8')
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(
        http_credentials={"username": config['HTTP CREDS']['username'],
                          "password": config['HTTP CREDS']['password']}
    )
    page = context.new_page()
    page.goto(config['PAGE']['Url'])

    page.get_by_text("B2B").click()
    page.get_by_role("button", name="Είσοδος στην Πλατφόρμα").click()

    page.get_by_placeholder("Αναζήτηση Αγοράς...").click()
    page.get_by_role("option", name=config['EXAMPLES']['example_market']).click()

    # Result 1
    r1_name = page.get_by_text("MONDELEZ ΕΛΛΑΣ ΑΕ ΕΜΠΟΡΙΑ ΣΟΚΟΛΑΤΑΣ ΚΑΙ ΤΥΠΟΠΟΙΗΜΕΝΩΝ ΤΡΟΦΙΜΩΝ").nth(0).inner_text()
    r1_afm_gemh_inDate = ' '.join(page.get_by_text("ΑΦΜ: 094191788 | ΓΕΜΗ: 000823401000 | Ίδρυση: Νοέμβριος 1987").nth(0).inner_text().split())
    r1_main_activity = page.get_by_text("ΧΟΝΔΡΙΚΟ ΕΜΠΟΡΙΟ ΤΥΠΟΠΟΙΗΜΕΝΩΝ ΖΑΧΑΡΩΔΩΝ ΠΡΟΪΟΝΤΩΝ").nth(0).inner_text()
    r1_phone = page.locator("[id=\"\\30 94191788\"]").get_by_role("img").nth(2)
    r1_email = page.locator("[id=\"\\30 94191788\"]").get_by_role("img").nth(3)
    r1_website = page.locator("[id=\"\\30 94191788\"]").get_by_role("img").nth(4)

    assert r1_name == "MONDELEZ ΕΛΛΑΣ ΑΕ ΕΜΠΟΡΙΑ ΣΟΚΟΛΑΤΑΣ ΚΑΙ ΤΥΠΟΠΟΙΗΜΕΝΩΝ ΤΡΟΦΙΜΩΝ"
    assert r1_afm_gemh_inDate  == "ΑΦΜ: 094191788 | ΓΕΜΗ: 000823401000 | Ίδρυση: Νοέμβριος 1987 | Εταιρικός Τύπος: ΑΕ"
    assert r1_main_activity == "ΧΟΝΔΡΙΚΟ ΕΜΠΟΡΙΟ ΤΥΠΟΠΟΙΗΜΕΝΩΝ ΖΑΧΑΡΩΔΩΝ ΠΡΟΪΟΝΤΩΝ"
    assert r1_phone is not None
    assert r1_email is not None
    assert r1_website is not None

    # Result 2
    r2_name = page.get_by_text("ΙΟΝ ΑΝΩΝΥΜΗ ΕΤΑΙΡΕΙΑ ΒΙΟΜΗΧΑΝΙΑΣ ΚΑΙ ΕΜΠΟΡΙΟΥ ΚΑΚΑΟ ΚΑΙ ΣΟΚΟΛΑΤΑΣ").nth(0).inner_text()
    r2_afm_gemh_inDate = ' '.join(page.get_by_text("ΑΦΜ: 094006864 | ΓΕΜΗ: 121545307000 | Ίδρυση: Σεπτέμβριος 1930").nth(0).inner_text().split())
    r2_main_activity = page.get_by_text("ΠΑΡΑΓΩΓΗ ΚΑΚΑΟΥ, ΣΟΚΟΛΑΤΑΣ ΚΑΙ ΖΑΧΑΡΩΤΩΝ").nth(0).inner_text()
    r2_phone = page.locator("[id=\"\\30 94006864\"]").get_by_role("img").nth(2)
    r2_email = page.locator("[id=\"\\30 94006864\"]").get_by_role("img").nth(3)
    r2_website = page.locator("[id=\"\\30 94006864\"]").get_by_role("img").nth(4)

    assert r2_name == "ΙΟΝ ΑΝΩΝΥΜΗ ΕΤΑΙΡΕΙΑ ΒΙΟΜΗΧΑΝΙΑΣ ΚΑΙ ΕΜΠΟΡΙΟΥ ΚΑΚΑΟ ΚΑΙ ΣΟΚΟΛΑΤΑΣ"
    assert r2_afm_gemh_inDate == "ΑΦΜ: 094006864 | ΓΕΜΗ: 121545307000 | Ίδρυση: Σεπτέμβριος 1930 | Εταιρικός Τύπος: ΑΕ"
    assert r2_main_activity == "ΠΑΡΑΓΩΓΗ ΚΑΚΑΟΥ, ΣΟΚΟΛΑΤΑΣ ΚΑΙ ΖΑΧΑΡΩΤΩΝ"
    assert r2_phone is not None
    assert r2_email is not None
    assert r2_website is not None

    # Result 3
    r3_name = page.get_by_text("ΖΑΧΑΡΟΠΛΑΣΤΕΙΟ ΠΑΝΤΑΖΗΣ ΙΔΙΩΤΙΚΗ ΚΕΦΑΛΑΙΟΥΧΙΚΗ ΕΤΑΙΡΕΙΑ")
    r3_afm_gemh_inDate = ' '.join(page.get_by_text("ΑΦΜ: 801354084 | ΓΕΜΗ: 154983342000 | Ίδρυση: Ιούνιος 2020").nth(0).inner_text().split())
    r3_main_activity = page.get_by_text("ΠΑΡΑΓΩΓΗ ΝΩΠΩΝ ΕΙΔΩΝ ΖΑΧΑΡΟΠΛΑΣΤΙΚΗΣ ΚΑΙ ΓΛΥΚΙΣΜΑΤΩΝ").nth(0).inner_text()
    r3_phone = page.locator("[id=\"\\38 01354084\"]").get_by_role("img").nth(2)
    r3_email = page.locator("[id=\"\\38 01354084\"]").get_by_role("img").nth(3)
    r3_website = page.locator("[id=\"\\38 01354084\"]").get_by_role("img").nth(4)

    assert r3_name is not None
    assert r3_afm_gemh_inDate == "ΑΦΜ: 801354084 | ΓΕΜΗ: 154983342000 | Ίδρυση: Ιούνιος 2020 | Εταιρικός Τύπος: ΙΚΕ"
    assert r3_main_activity == "ΠΑΡΑΓΩΓΗ ΝΩΠΩΝ ΕΙΔΩΝ ΖΑΧΑΡΟΠΛΑΣΤΙΚΗΣ ΚΑΙ ΓΛΥΚΙΣΜΑΤΩΝ"
    assert r3_phone is not None
    assert r3_email is not None
    assert r3_website is not None

    # Result 4
    r4_name = page.get_by_text("ΠΑΡΑΓΩΓΗ ΕΙΔΩΝ ΖΑΧΑΡΟΠΛΑΣΤΙΚΗΣ ΠΑΓΩΤΩΝ ΑΝΩΝΥΜΟΣ ΒΙΟΜΗΧΑΝΙΚΗ ΕΤΑΙΡΕΙΑ").nth(0).inner_text()
    r4_afm_gemh_inDate = ' '.join(page.get_by_text("ΑΦΜ: 095483297 | ΓΕΜΗ: 036400616000 | Ίδρυση: Φεβρουάριος 1990").nth(0).inner_text().split())
    r4_main_activity = page.get_by_text("ΠΑΡΑΓΩΓΗ ΠΑΓΩΤΟΥ ΚΑΙ ΑΛΛΩΝ ΕΙΔΩΝ ΒΡΩΣΙΜΟΥ ΠΑΓΟΥ").nth(0).inner_text()
    r4_phone = page.locator("[id=\"\\30 95483297\"]").get_by_role("img").nth(2)
    r4_email = page.locator("[id=\"\\30 95483297\"]").get_by_role("img").nth(3)
    r4_website = page.locator("[id=\"\\30 95483297\"]").get_by_role("img").nth(4)

    assert r4_name == "ΠΑΡΑΓΩΓΗ ΕΙΔΩΝ ΖΑΧΑΡΟΠΛΑΣΤΙΚΗΣ ΠΑΓΩΤΩΝ ΑΝΩΝΥΜΟΣ ΒΙΟΜΗΧΑΝΙΚΗ ΕΤΑΙΡΕΙΑ"
    assert r4_afm_gemh_inDate == "ΑΦΜ: 095483297 | ΓΕΜΗ: 036400616000 | Ίδρυση: Φεβρουάριος 1990 | Εταιρικός Τύπος: ΑΕ"
    assert r4_main_activity == "ΠΑΡΑΓΩΓΗ ΠΑΓΩΤΟΥ ΚΑΙ ΑΛΛΩΝ ΕΙΔΩΝ ΒΡΩΣΙΜΟΥ ΠΑΓΟΥ"
    assert r4_phone is not None
    assert r4_email is not None
    assert r4_website is not None

    # Result 5
    r5_name = page.get_by_text("Σ ΚΑΝΔΥΛΑΣ ΑΝΩΝΥΜΗ ΕΤΑΙΡΙΑ").nth(0).inner_text()
    r5_afm_gemh_inDate = ' '.join(page.get_by_text("ΑΦΜ: 998530738 | ΓΕΜΗ: 021159526000 | Ίδρυση: Ιούνιος 2007").nth(0).inner_text().split())
    r5_main_activity = page.get_by_text("ΠΑΡΑΓΩΓΗ ΧΑΛΒΑΔΩΝ, ΚΟΥΦΕΤΩΝ ΚΑΙ ΛΟΥΚΟΥΜΙΩΝ").nth(0).inner_text()
    r5_phone = page.locator("[id=\"\\39 98530738\"]").get_by_role("img").nth(2)
    r5_email = page.locator("[id=\"\\39 98530738\"]").get_by_role("img").nth(3)
    r5_website = page.locator("[id=\"\\39 98530738\"]").get_by_role("img").nth(4)

    assert r5_name == "Σ ΚΑΝΔΥΛΑΣ ΑΝΩΝΥΜΗ ΕΤΑΙΡΙΑ"
    assert r5_afm_gemh_inDate  == "ΑΦΜ: 998530738 | ΓΕΜΗ: 021159526000 | Ίδρυση: Ιούνιος 2007 | Εταιρικός Τύπος: ΑΕ"
    assert r5_main_activity == "ΠΑΡΑΓΩΓΗ ΧΑΛΒΑΔΩΝ, ΚΟΥΦΕΤΩΝ ΚΑΙ ΛΟΥΚΟΥΜΙΩΝ"
    assert r5_phone is not None
    assert r5_email is not None
    assert r5_website is not None

    context.close()
    browser.close()
