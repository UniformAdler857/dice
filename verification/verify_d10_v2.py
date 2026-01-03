from playwright.sync_api import sync_playwright

def verify_d10_v2():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("http://localhost:8080/index.html")

        # Select D10 v2 from dropdown
        page.select_option("#diceType", "d10_v2")

        # Wait for dice to render (canvas)
        page.wait_for_timeout(2000)

        # Roll the dice
        page.click("#btnRoll")

        # Wait for roll to complete
        page.wait_for_timeout(3000)

        # Take screenshot
        page.screenshot(path="verification/d10_v2_verification.png")

        browser.close()

if __name__ == "__main__":
    verify_d10_v2()
