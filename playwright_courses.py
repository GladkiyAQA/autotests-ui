from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    email_field = page.get_by_test_id('registration-form-email-input').locator('input')
    email_field.fill('user.name@gmail.com')

    username_field = page.get_by_test_id('registration-form-username-input').locator('input')
    username_field.fill('username')

    password_field = page.get_by_test_id('registration-form-password-input').locator('input')
    password_field.fill('password')

    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    context.storage_state(path="browser-state.json")

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json")
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    courses_toolbar_title = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_toolbar_title).to_be_visible()
    expect(courses_toolbar_title).to_have_text('Courses')

    folder_icon = page.get_by_test_id('courses-list-empty-view-icon')
    expect(folder_icon).to_be_visible()

    view_title_text = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(view_title_text).to_be_visible()
    expect(view_title_text).to_have_text('There is no results')

    description_rext = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(description_rext).to_be_visible()
    expect(description_rext).to_have_text('Results from the load test pipeline will be displayed here')
