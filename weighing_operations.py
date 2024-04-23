from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def weigh_groups(driver, group1, group2):
    weigh_button = driver.find_element(By.ID, "weigh")
    time.sleep(1)
    for coin in range(len(group1)):
        ids = "left_" + str(coin)
        val = driver.find_element(By.ID, ids)
        val.click()
        time.sleep(0.5)
        val.send_keys(str(group1[coin]))
        time.sleep(1)
    for coin in range(len(group2)):
        ids = "right_" + str(coin)
        val = driver.find_element(By.ID, ids)
        val.click()
        time.sleep(0.5)
        val.send_keys(str(group2[coin]))
        time.sleep(1)
    weigh_button.click()
    time.sleep(3)
    result = driver.find_element(By.CLASS_NAME, "result").text
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[text()='Reset']").click()
    return result

def same_group_weigh(driver, group1, group2):
    weigh_button = driver.find_element(By.ID, "weigh")
    time.sleep(1)
    val = driver.find_element(By.ID, "left_0")
    val.click()
    time.sleep(0.5)
    val.send_keys(str(group1))
    time.sleep(1)
    val = driver.find_element(By.ID, "right_0")
    val.click()
    time.sleep(0.5)
    val.send_keys(str(group2))
    time.sleep(1)
    weigh_button.click()
    time.sleep(3)
    result = driver.find_element(By.CLASS_NAME, "result").text
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[text()='Reset']").click()
    return result

def alert_handler(driver, bar_id):
    # alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
    id = "coin_"+str(bar_id)
    driver.find_element(By.ID, id).click()
    alert = driver.switch_to.alert
    alert_text = alert.text
    time.sleep(2)
    alert.accept()
    res  = driver.find_element(By.CLASS_NAME, "game-info").text
    print(res)
    print(f"{alert_text} the fake bar is {bar_id}")
