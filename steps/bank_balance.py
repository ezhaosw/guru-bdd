from steps.locators import BankBalanceLocators
from utils import page_utils


class BankBalance:

    def __init__(self, driver):
        self.driver = driver

    def on_page(self):
        return page_utils.on_page(
            self.driver,
            BankBalanceLocators.DETAILS
        )
