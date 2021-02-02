from selenium.webdriver.common.by import By


class BankHomeLocators:
    ID_FIELD = (
        By.CSS_SELECTOR,
        'input[name="uid"]'
    )
    PWD_FIELD = (
        By.CSS_SELECTOR,
        'input[name="password"]'
    )
    LOGIN_BUTTON = (
        By.CSS_SELECTOR,
        'input[name="btnLogin"]'
    )


class BankProfileLocators:
    WELCOME = (
        By.XPATH,
        '//*[contains(text(), "Welcome")]'
    )
    BALANCE_LINK = (
        By.LINK_TEXT,
        'Balance Enquiry'
    )


class BankEnquiryLocators:
    HEADING = (
        By.XPATH,
        '//*[contains(text(), "Balance Enquiry Form")]'
    )
    DROPDOWN = (
        By.CSS_SELECTOR,
        'select[name="accountno"]'
    )
    SUBMIT = (
        By.CSS_SELECTOR,
        'input[name="AccSubmit"]'
    )


class BankBalanceLocators:
    DETAILS = (
        By.XPATH,
        '//*[contains(text(), "Balance Details for Account")]'
    )
