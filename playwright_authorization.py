import time

from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    email_field = page.get_by_test_id("login-form-email-input").locator("input")
    email_field.fill("user.name@gmail.com")

    password_field = page.get_by_test_id("login-form-password-input").locator("input")
    password_field.fill("password")

    login_button = page.get_by_test_id("login-page-login-button")
    login_button.click()

    alert_message = page.get_by_test_id("login-page-wrong-email-or-password-alert")
    expect(alert_message).to_be_visible()
    expect(alert_message).to_have_text("Wrong email or password")
    time.sleep(5)