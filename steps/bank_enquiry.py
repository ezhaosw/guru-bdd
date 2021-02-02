from steps.locators import BankEnquiryLocators
from steps.bank_balance import BankBalance
from selenium.webdriver.support.select import Select
from utils import page_utils


class BankEnquiry:

    def __init__(self, driver):
        self.driver = driver

    def on_page(self):
        return page_utils.on_page(
            self.driver,
            BankEnquiryLocators.HEADING
        )

    def select_account(self, account_id):
        dropdown = self.driver.find_element(
            *BankEnquiryLocators.DROPDOWN
        )
        select = Select(dropdown)
        select.select_by_visible_text(account_id)

    def submit_choice(self):
        submit_btn = self.driver.find_element(
            *BankEnquiryLocators.SUBMIT
        )
        submit_btn.click()

        return BankBalance(self.driver)
