from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.tutorialspoint.com/selenium/practice/frames.php")
    # normal text
    normalTxt = page.locator("//h2[normalize-space()='Iframe 1']").text_content()
    print(normalTxt)

    # iframe text
    framTxt = page.frame_locator("iframe[src='new-tab-sample.php']").first.locator("a[class='external-link']").text_content()
    print(framTxt)

    page.close()
