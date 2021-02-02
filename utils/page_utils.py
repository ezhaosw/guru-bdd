def on_page(driver, selector):
    found = driver.find_elements(*selector)
    return len(found) > 0
