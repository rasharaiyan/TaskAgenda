class LateAllEventsPage:
    #this page is for all events screen and late events screen
    def __init__(self, driver):
        self.driver = driver
        # Locators
        self.search_button = 'com.claudivan.taskagenda:id/etSearch'
        self.filter_button = '(//android.widget.LinearLayout[@resource-id="com.claudivan.taskagenda:id/content"])[1]'
        self.not_completed_button = '//android.widget.TextView[@resource-id="com.claudivan.taskagenda:id/title" and @text="Not completed"]'
        self.date_button = '(//android.widget.LinearLayout[@resource-id="com.claudivan.taskagenda:id/content"])[2]'
        self.type_button = '//android.widget.TextView[@resource-id="com.claudivan.taskagenda:id/title" and @text="Type"]'

    def open_search(self):
        """Opens the search bar to type in."""
        self.driver.find_element_by_id(self.search_button).click()

    def enter_search_query(self, query):
        search_element = self.driver.find_element_by_id(self.search_button)
        search_element.clear()
        search_element.send_keys(query)

    def apply_filter(self):
        self.driver.find_element_by_xpath(self.filter_button).click()

    def select_not_completed(self):
        self.driver.find_element_by_xpath(self.not_completed_button).click()

    def filter_by_date(self):
        self.driver.find_element_by_xpath(self.date_button).click()

    def filter_by_type(self):
        self.driver.find_element_by_xpath(self.type_button).click()
