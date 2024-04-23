from webdriver_setup import setup_driver
from weighing_operations import weigh_groups, same_group_weigh, alert_handler
import time

def find_fake_brick(driver):
    try:
        # Best way to find the fake brick is to divide the 9 bricks into 3  groups of 3.
        groupA, groupB, groupC = [0, 1, 2], [3, 4, 5], [6, 7, 8]
        result_1 = weigh_groups(driver, groupA, groupB)
        #if the first 2 groups are equal than the fake brick is in the 3rd group and if any of the first 2 group is smaller than the other 
        #the fake brick is the smaller group
        if "=" in result_1:
            result_2 = same_group_weigh(driver, groupC[0], groupC[1])
            if "=" in result_2:
                alert_handler(driver, 8)
            elif ">" in result_2:
                alert_handler(driver, 7)
            else:
                alert_handler(driver, 6)
        elif "<" in result_1:
            result_2 = same_group_weigh(driver, groupA[0], groupA[1])
            if "=" in result_2:
                alert_handler(driver, 2)
            elif ">" in result_2:
                alert_handler(driver, 1)
            else:
                alert_handler(driver, 0)
        else:
            result_2 = same_group_weigh(driver, groupB[0], groupB[1])
            if "=" in result_2:
                alert_handler(driver, 5)
            elif ">" in result_2:
                alert_handler(driver, 4)
            else:
                alert_handler(driver, 3)
    except Exception as e:
        alert = driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        driver.quit()
    finally:
        driver.quit()

def main():
    driver = setup_driver()
    find_fake_brick(driver)

if __name__ == "__main__":
    main()
