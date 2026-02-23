from time import sleep

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
    page.wait_for_selector("//input[@id='name']")
    page.fill("//input[@id='name']", "John Doe")
    page.click("#gender")
    page.wait_for_timeout(2000)
    page.click("#hobbies")
    # page.fill("//input[@id='picture']", "images/screenshot.png")
    sleep(2)
    page.select_option("//select[@id='state']",index=2)
    sleep(1)
    page.select_option("//select[@id='state']", "NCR")
    sleep(1)
    page.select_option("//select[@id='state']", label="Rajasthan")
    page.wait_for_load_state("networkidle")
    sleep(1)
    page.screenshot(path="images/screenshot.png")

    # page.locator("input[value='Login']").scroll_into_view_if_needed()
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

    page.close()
