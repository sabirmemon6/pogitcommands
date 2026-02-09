from utilities import configReader


class CarBase:

    def __init__(self, page):
        self.page = page

    def getCarTitle(self):
        return self.page.locator(configReader.readConfig("locators", "carTitle_XPATH")).inner_text()

    def getCarNameAndPrices(self):
        carNames = self.page.locator(configReader.readConfig("locators", "carName_XPATH"))
        carPrices = self.page.locator(configReader.readConfig("locators", "carPrice_XPATH"))
        print(f"Car prices length are : {carPrices.count()}")

        #adding comments
        for i in range(1, carPrices.count()):
            print((carNames.nth(i).inner_text()+"----Prices are-----"+carPrices.nth(i).inner_text()).encode('utf8'))


