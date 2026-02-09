from pages.BMWPage import BMWPage
from pages.BasePage import BasePage
from pages.HondaPage import HondaPage
from pages.MGPage import MGPage
from pages.ToyotaPage import ToyotaPage


class NewCarsPage(BasePage):

    def __init__(self, page):
        super().__init__(page)


    def selectToyota(self):
        self.click("toyota_XPATH")
        return ToyotaPage(self.page)  # method chaining

    def selectBMW(self):
        self.click("Bmw_XPATH")
        return BMWPage(self.page)  # method chaining

    def selectHonda(self):
        self.click("honda_XPATH")
        return HondaPage(self.page)  # method chaining

    def selectMG(self):
        self.click("MG_XPATH")
        return MGPage(self.page)  # method chaining

