# import configparser
#
# from playwright.sync_api import Playwright, Page, expect
#
#
# def test_case_id_26(playwright: Playwright):
#     config = configparser.ConfigParser()
#     config.read('config.env', 'utf-8')
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto(config['PAGE']['Url'])
#
#     # Successful Login
#     page.get_by_role("button", name="Είσοδος").click()
#     page.get_by_placeholder("Email").click()
#     page.get_by_placeholder("Email").fill(config['USER']['Email'])
#     page.get_by_placeholder("Password").click()
#     page.get_by_placeholder("Password").fill(config['USER']['Password'])
#     page.get_by_role("button", name="Είσοδος").click()
#
#     page.get_by_role("button", name="ΕΙΣΟΔΟΣ ΣΤΟ B2B").click()
#
#     page.get_by_role("link", name="B2B Dashboard").click()
#     # click on first purchased lead
#     page.get_by_text("Ξενοδοχεία" + " " + config['EXAMPLES']['b2bHotCnt_univ']).first.click()
#     # click on "Εταιρικό Report" of the first result in the purchased lead
#     page.locator(f"[id=\"\\38 {int(config['EXAMPLES']['v6'])}\"]").get_by_role("button", name="Εταιρικό Report").click()
#     expect(page).to_have_url(config['PAGE']['UrlKYCl'] + "/" + config['EXAMPLES']['v6'] + "/" + "overview")
#
#     context.close()
#     browser.close()
