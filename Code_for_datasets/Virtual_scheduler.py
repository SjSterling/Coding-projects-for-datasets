from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()

        page = context.new_page()
        page.goto('https://vsb.valdosta.edu/criteria.jsp')  # Replace with your URL
        username_selector = 'input#userNameInput'
        password_selector = 'input#passwordInput'

        page.fill(username_selector, 'sjscarlett@valdosta.edu')
        page.fill(password_selector, 'GAkings03')

        # Click the "Sign In" button
        sign_in_selector = 'span#submitButton'
        page.click(sign_in_selector)

        # Wait for the element to become available
        element_selector = 'a.term-card-title[href*=\'202308\']'
        page.wait_for_selector(element_selector, state='visible')

        # Click the element using JavaScript evaluation
        page.evaluate(f'document.querySelector("{element_selector}").click()')

        page.wait_for_load_state('networkidle')
        page.screenshot(path='schedule_screenshot.png')
        page.close()

if __name__ == '__main__':
    main()

