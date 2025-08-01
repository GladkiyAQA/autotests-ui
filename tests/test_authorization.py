import pytest
from playwright.sync_api import sync_playwright, expect
from pages.login_page import LoginPage

@pytest.mark.parametrize(
    "email, password",
    [
        ("user.name@gmail.com", "password"),
        ("user.name@gmail.com", "  "),
        ("  ", "password"),
    ],
    ids=[
        "invalid_email_and_password",
        "invalid_email_and_empty_password",
        "empty_email_and_invalid_password"
    ]
)
def test_wrong_email_or_password_authorization(login_page: LoginPage, email: str, password: str):
    login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
    login_page.fill_login_form(email=email, password=password)
    login_page.click_login_button()
    login_page.check_visible_wrong_email_or_password_alert()
