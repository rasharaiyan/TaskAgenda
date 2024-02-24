
import unittest
from selenium import webdriver
from appium import webdriver as appium_webdriver
from logic.task_page import TaskPage
from infra.task_agenda_app import DriverManager


class TestAddTask(unittest.TestCase):


    def test_add_new_task(self):
        task_page = TaskPage(self.driver)

        # Navigate to the Add Task page
        task_page.navigate_to_add_task()

        # Enter event details
        task_page.enter_event_name("New Task Name")
        task_page.enter_event_description("This is a detailed description of the new task.")

        # Set time and date for the task
        task_page.set_time("10", "30")
        task_page.set_date("25", "12", "2024")

        # Select task type
        task_page.select_type("Important")

        # Save the event
        task_page.save_event()




if __name__ == '__main__':
    unittest.main()
