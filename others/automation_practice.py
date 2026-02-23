from time import sleep

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
    page.fill("#name", "Rohan")
    page.fill("#email", "abcd@gmail.com")
    sleep(2)
    page.click("#gender")
    sleep(2)
    page.click("#hobbies")
    sleep(2)
    page.locator("//select[@id='state']").scroll_into_view_if_needed()
    page.select_option("//select[@id='state']", "Haryana")
    sleep(2)
    page.select_option("//select[@id='state']", index=1)
    sleep(2)
    page.select_option("//select[@id='state']", label="Rajasthan")
    sleep(2)

    page.close()