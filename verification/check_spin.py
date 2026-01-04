from playwright.sync_api import sync_playwright

def verify_spin():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("http://localhost:3000")

        # Click roll
        page.click("button#btnRoll")

        # Wait a bit for spin to happen
        page.wait_for_timeout(1000)

        # Take screenshot
        page.screenshot(path="verification/spin_check.png")

        browser.close()

if __name__ == "__main__":
    verify_spin()
