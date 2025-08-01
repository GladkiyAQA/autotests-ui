import pytest
from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage


@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(
        registration_page: RegistrationPage,
        dashboard_page: DashboardPage,
):
    registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    registration_page.fill_login_form(
        email='user@gmail.com',
        username='password',
        password='username'
    ),
    registration_page.click_registration_button()
    dashboard_page.check_visible_dashboard_title()