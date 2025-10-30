from pages.base_page import BasePage
from playwright.sync_api import expect, Page

class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.dashboard_title_text = page.get_by_test_id('dashboard-toolbar-title-text')

    def check_visible_dashboard_title(self):
        expect(self.dashboard_title_text).to_be_visible()
        expect(self.dashboard_title_text).to_have_text('Dashboard')