from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    # page.goto("https://www.tutorialspoint.com/selenium/practice/scroll-down.php")
    page.goto("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
    page.wait_for_timeout(3000)
    # page.evaluate("window.scrollTo(0, document.body.scrollHeight)") # scroll to the bottom of the page
    # page.evaluate("window.scrollBy(0, 600)") # scroll 600px down
    page.evaluate("document.querySelector('#picture').scrollIntoView()") # scroll 600px down
    page.wait_for_timeout(3000)
    page.close()