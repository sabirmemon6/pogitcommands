
from utilities import configReader
import logging
from utilities.LogUtil import Logger
import allure

log = Logger(__name__, logging.INFO)


class BasePage:

    def __init__(self, page):
        self.page = page

  #creating Keywords, Click(), Type()

    def click(self, locator):
        with allure.step("Clicking on an Element"):
          self.page.locator(configReader.readConfig("locators", locator)).click()
          log.logger.info("Clicking on an element: " + str(locator))


    def type(self, locator, value):
        with allure.step("Typing in an Element"):
          self.page.locator(configReader.readConfig("locators", locator)).fill(value)
          log.logger.info("Typing in an element: " + str(locator) + " value entered as : " + str(value))


    def moveTo(self, locator):
        with allure.step("Moving to an Element"):
          self.page.locator(configReader.readConfig("locators", locator)).hover()
          log.logger.info("Moving to an element: " + str(locator))
