import pytest
from appium import webdriver
from logic.late_all_events_page import AllEventsPage
from infra.task_agenda_app import DriverManager



def test_search_events(driver):
    all_events_page = AllEventsPage(driver)
    all_events_page.open_search()
    all_events_page.enter_search_query("Meeting")


def test_filter_not_completed_events(driver):
    all_events_page = AllEventsPage(driver)
    all_events_page.apply_filter()
    all_events_page.select_not_completed()


def test_filter_by_date(driver):
    all_events_page = AllEventsPage(driver)
    all_events_page.filter_by_date()


def test_filter_events_by_type(driver):
    all_events_page = AllEventsPage(driver)
    all_events_page.filter_by_type()
