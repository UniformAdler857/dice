from playwright.sync_api import sync_playwright

def verify_d10(page):
    # Navigate to the app (served on port 3000)
    page.goto("http://localhost:3000")

    # Wait for the app to load
    page.wait_for_selector("#diceType")

    # Select 'd10' from the dropdown
    page.select_option("#diceType", "d10")

    # Wait for the dice to be re-created
    page.wait_for_timeout(2000)

    # Take a screenshot of the 3D canvas
    page.screenshot(path="verification/d10_new.png")

    print("Screenshot saved to verification/d10_new.png")

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        try:
            verify_d10(page)
        except Exception as e:
            print(f"Error: {e}")
        finally:
            browser.close()
