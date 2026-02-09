from pages.BasePage import BasePage
from pages.NewCarsPage import NewCarsPage


class HomePage(BasePage):

    def __init__(self, page):
        super().__init__(page)


    def gotoNewCars(self):
        self.moveTo("newCar_XPATH")
        self.click("findNewCars_XPATH")

        return NewCarsPage(self.page)  #method chaining

    def gotoCompareCars(self):
        pass

    def gotoUsedCars(self):
        pass