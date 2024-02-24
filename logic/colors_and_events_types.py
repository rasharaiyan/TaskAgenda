class ColorsEventsTypes:
    def __init__(self, driver):
        self.driver = driver
        # Locators
        self.main_color_choose = '//android.widget.LinearLayout[@resource-id="com.claudivan.taskagenda:id/item_background"]/android.view.View'
        self.dark_mode = '//android.widget.LinearLayout[@resource-id="com.claudivan.taskagenda:id/itemTemaEscuro"]'
        self.event_widget_color_choose = '//android.widget.LinearLayout[@resource-id="com.claudivan.taskagenda:id/item_widget_eventos"]/android.view.View'
        self.add_new_event_type = '//android.widget.TextView[@text="Add new"]'
        self.event_type_name = 'com.claudivan.taskagenda:id/etNome'
        self.color_event_type_choose = '//android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]'
        self.icon_event_type_choose = '//android.widget.TextView[@text="Icon"]'
        self.save_button = 'com.claudivan.taskagenda:id/item_salvar'

    def choose_main_color(self):
        """Selects the main color."""
        self.driver.find_element_by_xpath(self.main_color_choose).click()

    def toggle_dark_mode(self):
        """Toggles the dark mode setting."""
        self.driver.find_element_by_xpath(self.dark_mode).click()

    def choose_event_widget_color(self):
        """Selects the event widget color."""
        self.driver.find_element_by_xpath(self.event_widget_color_choose).click()

    def add_new_event_type(self):
        """Navigates to add a new event type."""
        self.driver.find_element_by_xpath(self.add_new_event_type).click()

    def enter_event_type_name(self, name):
        """Enters the name for the new event type."""
        self.driver.find_element_by_id(self.event_type_name).send_keys(name)

    def choose_color_for_event_type(self):
        """Chooses a color for the new event type."""
        self.driver.find_element_by_xpath(self.color_event_type_choose).click()

    def choose_icon_for_event_type(self):
        """Chooses an icon for the new event type."""
        self.driver.find_element_by_xpath(self.icon_event_type_choose).click()

    def save_event_type(self):
        """Saves the new event type."""
        self.driver.find_element_by_id(self.save_button).click()
