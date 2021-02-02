from steps.locators import BankProfileLocators
from steps.bank_enquiry import BankEnquiry
from utils import page_utils


class BankProfile:

    def __init__(self, driver):
        self.driver = driver

    def on_page(self):
        return page_utils.on_page(
            self.driver,
            BankProfileLocators.WELCOME
        )

    def check_balance(self):
        link = self.driver.find_element(
            *BankProfileLocators.BALANCE_LINK
        )
        link.click()
        return BankEnquiry(self.driver)


