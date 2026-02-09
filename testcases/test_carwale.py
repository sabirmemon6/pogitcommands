import time

import pytest

from pages.CarBase import CarBase
from pages.HomePage import HomePage
from pages.NewCarsPage import NewCarsPage
from testcases.BaseTest import BaseTest
from utilities import dataProvider
import allure


import logging
from utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)


class Test_CarWale(BaseTest):

    @allure.feature("Login Test")
    @allure.severity(allure.severity_level.MINOR)
    #@pytest.mark.skip
    def test_gotoNewCar(self,page):
        log.logger.info("******Inside New Car Test*********")
        with allure.step("Inside New Car Test"):
          home = HomePage(page)
          home.gotoNewCars()
    #Creating objects of class, lets doing method chaining to avoid create object of every class.
          #Method should return the object of class. gotoNewCars()
          #newCars=NewCarsPage(page)
          #toyotaCars=ToyotaPage(page)
          # time.sleep(3)

    #@pytest.mark.skip
    @allure.feature("Login Test")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("carBrand,carTitle",dataProvider.get_data("NewCarsTest"))
    #def test_select_cars(self,page, carBrand,carTitle)
    def test_select_cars(self, page, carBrand, carTitle):
        log.logger.info("******Inside Select Cars Test*********")
        home = HomePage(page)

        #home.gotoNewCars()
        #time.sleep(3000)

        car = CarBase(page)

        print("Car brand is : ",carBrand)

        if carBrand == "BMW":

           home.gotoNewCars().selectBMW()
           title = car.getCarTitle()
           print("Car Title is : "+title)
           assert title == carTitle, "Not on the correct page as title is not matching"
        elif carBrand == "MG":
           home.gotoNewCars().selectMG()
           title = car.getCarTitle()
           print("Car Title is : " + title)
           assert title == carTitle, "Not on the correct page as title is not matching"
        elif carBrand == "Honda":
           home.gotoNewCars().selectHonda()
           title = car.getCarTitle()
           print("Car Title is : " + title)
           assert title == carTitle, "Not on the correct page as title is not matching"
        elif carBrand == "Toyota":
           home.gotoNewCars().selectToyota()
           title = car.getCarTitle()
           print("Car Title is : " + title)
           assert title == carTitle, "Not on the correct page as title is not matching"

    #@pytest.mark.skip
    @allure.feature("Login Test")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("carBrand,carTitle",dataProvider.get_data("NewCarsTest"))
    def test_print_car_names_and_prices(self,page, carBrand,carTitle):
        log.logger.info("******Inside Car Names and Prices Test*********")
        home = HomePage(page)
        car = CarBase(page)

        print("Car brand is : ",carBrand)
        if carBrand == "BMW":
           home.gotoNewCars().selectBMW()
           title = car.getCarTitle()
           print(("Car Title is : "+title))
           assert title == carTitle, "Not on the correct page as title is not matching"
           car.getCarNameAndPrices()
        elif carBrand == "MG":
           home.gotoNewCars().selectMG()
           title = car.getCarTitle()
           print(("Car Title is : " + title))
           assert title == carTitle, "Not on the correct page as title is not matching"
           car.getCarNameAndPrices()
        elif carBrand == "Honda":
           home.gotoNewCars().selectHonda()
           title = car.getCarTitle()
           print(("Car Title is : " + title))
           assert title == carTitle, "Not on the correct page as title is not matching"
           car.getCarNameAndPrices()
        elif carBrand == "Toyota":
           home.gotoNewCars().selectToyota()
           title = car.getCarTitle()
           print(("Car Title is : " + title))
           assert title == carTitle, "Not on the correct page as title is not matching"
           car.getCarNameAndPrices()
