from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class TaskPage:
    def __init__(self, driver):
        self.driver = driver
        # Locators
        self.add_task_button = 'com.claudivan.taskagenda:id/btNovoEvento'
        self.event_name_field = 'com.claudivan.taskagenda:id/etTitulo'
        self.event_description_field = 'com.claudivan.taskagenda:id/etDescricao'
        self.time_option = 'com.claudivan.taskagenda:id/btHora'
        self.date_selector = 'com.claudivan.taskagenda:id/btData'
        self.type = 'com.claudivan.taskagenda:id/vgItemEtiqueta'
        self.type_important = "Important"
        self.type_task = "Task"
        self.type_not_forget = "Not Forget"
        self.navigate_app = '//android.widget.ImageButton[@content-desc="Navigate up"]'
        self.menu= 'com.claudivan.taskagenda:id/vgItemEtiqueta'
        self.save_event_button = 'com.claudivan.taskagenda:id/item_salvar'

    def navigate_to_add_task(self):
        self.driver.find_element_by_id(self.add_task_button).click()

    def enter_event_name(self, name):
        self.driver.find_element_by_id(self.event_name_field_field).send_keys(name)

    def enter_event_description(self, description):
        self.driver.find_element_by_id(self.event_description_field).send_keys(description)

    def set_time(self, hour, minute):
        self.driver.find_element_by_id(self.time_option).click()
        self.driver.find_element_by_accessibility_id("Select hours").send_keys(hour)
        self.driver.find_element_by_accessibility_id("Select minutes").send_keys(minute)
        # Confirm the date
        self.driver.find_element_by_id("android:id/button1").click()  # "OK" button

    def set_date(self, day, month, year):
        # Open the DatePicker
        self.driver.find_element_by_id(self.date_selector).click()

        # Wait for DatePicker to be visible
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "android:id/datePicker"))
        )
        # Select the year
        self.driver.find_element_by_id("android:id/date_picker_header_year").click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, f"//android.widget.TextView[@text='{year}']"))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, f"//android.widget.TextView[@text='{month}']"))
        ).click()

        # Select the day
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//android.widget.TextView[@text='{day}']"))
        ).click()

        # Confirm the date
        self.driver.find_element_by_id("android:id/button1").click()  # "OK" button

    def select_type(self, task_type):
        self.driver.find_element_by_id(self.type).click()

        task_type_to_select = {
            'Important': self.type_important,
            'Task': self.type_task,
            'Not Forget': self.type_not_forget
        }.get(task_type)

        if task_type_to_select:

            self.driver.find_element_by_android_uiautomator(f'new UiSelector().text("{task_type_to_select}")').click()
        else:
            raise ValueError(f"Unsupported task type: {task_type}")

    def navigate_back(self):
        self.driver.find_element_by_xpath(self.navigate_app).click()

    def save_event(self):
        self.driver.find_element_by_id(self.save_event_button).click()

    def open_menu(self):
        self.driver.find_element_by_id(self.menu).click()
