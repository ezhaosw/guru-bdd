from selenium import webdriver


def before_all(context):
    context.driver = webdriver.Chrome(
        executable_path=r'/opt/webdriver/bin/chromedriver'
    )


def after_all(context):
    context.driver.quit()
