import unittest
from selenium import webdriver
from appium import webdriver as appium_webdriver
from infra.task_agenda_app import DriverManager
from logic.menu_page import MenuPage

class TestMenuNavigation(unittest.TestCase):

    def test_navigate_to_all_events(self):
        menu_page = MenuPage(self.driver)
        menu_page.go_to_all_events()
        self.assertTrue(self.wait.until(EC.presence_of_element_located(
            (By.XPATH, '//android.widget.TextView[@text="All events"]'))))

    def test_navigate_to_late_events(self):
        menu_page = MenuPage(self.driver)
        menu_page.go_to_late_events()
        # Example assertion for Late Events page
        self.assertTrue(self.wait.until(EC.presence_of_element_located
                                        ((By.ID, 'com.claudivan.taskagenda:id/tvEventosAtrasados'))))

    def test_open_settings(self):
        menu_page = MenuPage(self.driver)
        menu_page.open_settings()
        self.assertTrue(self.wait.until(EC.presence_of_element_located(
            (By.XPATH, 'com.claudivan.taskagenda:id/btAjustes'))))

    def test_go_to_colors_and_events_types(self):
        menu_page = MenuPage(self.driver)
        menu_page.go_to_colors_and_events_types()
        self.assertTrue(
            self.wait.until(EC.presence_of_element_located((By.ID, 'specific_element_for_colors_and_events'))))


    def test_open_about(self):
        menu_page = MenuPage(self.driver)
        menu_page.open_about()
        self.assertTrue(self.wait.until(EC.presence_of_element_located((By.XPATH, 'com..taskagenda:id/btSobre'))))


if __name__ == '__main__':
    unittest.main()
