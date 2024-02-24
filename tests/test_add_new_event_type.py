import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium import webdriver as appium_webdriver
from logic.colors_and_events_types import ColorsEventsTypes
from infra.task_agenda_app import DriverManager


class TestColorsAndEventsTypes(unittest.TestCase):


    def test_colors_and_events_types(self):
        colors_events_types_page = ColorsEventsTypes(self.driver)

        # Toggle Dark Mode and verify
        colors_events_types_page.toggle_dark_mode()
        #assert
        self.assertTrue(self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="Dark mode activated"]'))))

        # Add new event type and verify fields are present
        colors_events_types_page.add_new_event_type()
        self.assertTrue(
            self.wait.until(EC.presence_of_element_located((By.ID, colors_events_types_page.event_type_name))))
        colors_events_types_page.enter_event_type_name("Meeting")
        # Choose color for event type and verify selection
        colors_events_types_page.choose_color_for_event_type()
        # Assuming there's a confirmation element or color change that can be checked
        self.assertTrue(self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="Color selected"]'))))

        # Choose icon for event type and verify selection
        colors_events_types_page.choose_icon_for_event_type()
         #assert
        self.assertTrue(self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="Icon selected"]'))))

        # Save the new event type and verify it was successful
        colors_events_types_page.save_event_type()
        #assert
        self.assertTrue(self.wait.until(EC.presence_of_element_located(
            (By.XPATH, '//android.widget.TextView[@text="Event type saved successfully"]'))))



if __name__ == '__main__':
    unittest.main()
