class MenuPage:
    def __init__(self, driver):
        self.driver = driver
        # Locators
        self.all_events_button = '//android.widget.TextView[@text="All events"]'
        self.late_events_button = 'com.claudivan.taskagenda:id/tvEventosAtrasados'
        self.settings_button = 'com.claudivan.taskagenda:id/btAjustes'
        self.colors_and_events_types = '//android.widget.TextView[@text="Colors and event types"]'
        self.about = 'com.claudivan.taskagenda:id/btSobre'

    def go_to_all_events(self):
        """Navigate to the All Events section."""
        self.driver.find_element_by_xpath(self.all_events_button).click()

    def go_to_late_events(self):
        """Navigate to the Late Events section."""
        self.driver.find_element_by_id(self.late_events_button).click()

    def open_settings(self):
        """Navigate to the Settings page."""
        self.driver.find_element_by_id(self.settings_button).click()

    def go_to_colors_and_events_types(self):
        """Navigate to the Colors and Event Types section."""
        self.driver.find_element_by_xpath(self.colors_and_events_types).click()

    def open_about(self):
        """Navigate to the About page."""
        self.driver.find_element_by_id(self.about).click()
