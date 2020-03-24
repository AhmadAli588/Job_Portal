from selenium import webdriver

nameidElem = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.ID, "username")))
nameidElem.send_keys(username)
pwdidElem = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.ID, "password")))
pwdidElem.send_keys(password)
continueElem = WebDriverWait(driver, 10).until(
    expected_conditions.presence_of_element_located((By.CLASS_NAME, "btn__primary--large")))
result = continueElem.submit()

search = WebDriverWait(driver, 10).until(
    expected_conditions.presence_of_element_located((By.XPATH, "//input[@placeholder='Search']"))).click()
WebDriverWait(driver, 10).until(
    expected_conditions.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']"))).send_keys('sports')
WebDriverWait(driver, 10).until(
    expected_conditions.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']"))).submit()