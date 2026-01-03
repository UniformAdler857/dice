from playwright.sync_api import sync_playwright

def verify_roll(page):
    page.goto("http://localhost:3000")
    page.select_option("#diceType", "d10")
    page.wait_for_timeout(1000)

    # Click Roll
    page.click("#btnRoll")

    # Wait for result to not be "-"
    page.wait_for_function("document.getElementById('currentResult').innerText !== '-'", timeout=10000)

    result = page.inner_text("#currentResult")
    print(f"Rolled a: {result}")

    page.screenshot(path="verification/d10_rolled.png")

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        try:
            verify_roll(page)
        except Exception as e:
            print(f"Error: {e}")
        finally:
            browser.close()
