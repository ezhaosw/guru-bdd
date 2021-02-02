from steps.locators import BankHomeLocators
from steps.bank_profile import BankProfile


class BankHome:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get('http://demo.guru99.com/v4/')

    def enter_id(self, user_id):
        id_field = self.driver.find_element(
            *BankHomeLocators.ID_FIELD
        )
        id_field.clear()
        id_field.send_keys(user_id)

    def enter_password(self, password):
        pwd_field = self.driver.find_element(
            *BankHomeLocators.PWD_FIELD
        )
        pwd_field.clear()
        pwd_field.send_keys(password)

    def login(self):
        login_button = self.driver.find_element(
            *BankHomeLocators.LOGIN_BUTTON
        )
        login_button.click()
        return BankProfile(self.driver)