from config.DriverChrome import DriverChrome
from config.Driver import Driver

def get_driver(browser):
    factory: Driver
    if browser == 'chrome':
        factory = DriverChrome()
        return factory.get_driver()
    else:
        raise Exception("Selected browser not supported")
