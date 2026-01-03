from playwright.sync_api import sync_playwright

def verify_d10_refactor(page):
    print("Navigating to app...")
    page.goto("http://localhost:3000")
    page.wait_for_selector("#diceType", state="visible")

    print("Selecting D10...")
    page.select_option("#diceType", "10")

    # Wait for the mesh to update (approximated by waiting a bit)
    page.wait_for_timeout(1000)

    print("Rolling...")
    page.click("#btnRoll")

    print("Waiting for result...")
    # Wait for the result text to change from "-" to something else
    page.wait_for_function("document.getElementById('currentResult').innerText !== '-'")

    result = page.inner_text("#currentResult")
    print(f"Rolled Result: {result}")

    print("Taking screenshots...")
    page.screenshot(path="verification/verification_refactor_shape.png")

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            verify_d10_refactor(page)
        except Exception as e:
            print(f"Error: {e}")
        finally:
            browser.close()
