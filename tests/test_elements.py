import time

from pages.base_page import BasePage
from pages.elements_page import TextBoxPage


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_cur_addr, output_per_addr = text_box_page.check_field_from()

            assert full_name == output_name, "The full name doesn't match"
            assert email == output_email, "The email name doesn't match"
            assert current_address == output_cur_addr, "The current address name doesn't match"
            assert permanent_address == output_per_addr, "The permanent address name doesn't match"


