import allure
from playwright.sync_api import Page
from components.base_component import BaseComponent
from elements.text import Text
from elements.button import Button

class CreateCourseToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.title = Text(page, "create-course-toolbar-title-text", "Create course title")
        self.create_course_button = Button(
            page, "create-course-toolbar-create-course-button", "Create course button"
        )

    @allure.step('Check visible "Create course" toolbar (button disabled = {is_create_course_disabled})')
    def check_visible(self, is_create_course_disabled: bool = True):
        self.title.check_visible()
        self.title.check_have_text("Create course")

        if is_create_course_disabled:
            self.create_course_button.check_disabled()
        else:
            self.create_course_button.check_enabled()

    @allure.step('Click "Create course" button')
    def click_create_course_button(self):
        self.create_course_button.click()
