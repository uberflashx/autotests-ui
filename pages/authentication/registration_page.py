from components.authentication.registration_form_component import RegistrationFormComponent
from pages.base_page import BasePage
from playwright.sync_api import Page
from elements.link import Link
from elements.button import Button
import re

class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.registration_form = RegistrationFormComponent(page)

        self.registration_button = Button(page, 'registration-page-registration-button', 'Registration')
        self.login_link = Link(page, 'registration-page-login-link', 'Login')
        self.user_already_exists_alert = page.get_by_test_id('registration-page-user-already-exists-alert')

    def click_login_link(self):
        self.login_link.click()
        self.check_current_url(re.compile(".*/#/auth/login"))

    def click_registration_button(self):
        self.registration_button.click()