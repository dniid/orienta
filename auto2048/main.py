import os
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def is_game_over(driver):
    """Returns true if game is over. Otherwise, returns False."""
    try:
        driver.find_element(By.CLASS_NAME, 'game-over')
        return True
    except NoSuchElementException:
        return False


def al_strategy(driver):
    """
    This strategy is from the book 'Automate the Boring Stuff with Python' by Al Sweigart.
    The strategy is to move up, right, down and then left and then repeat.
    """
    # Repeating the html element getter is necessary to avoid browser refresh errors
    html_elem = driver.find_element(By.TAG_NAME, 'html')
    html_elem.send_keys(Keys.UP)

    html_elem = driver.find_element(By.TAG_NAME, 'html')
    html_elem.send_keys(Keys.RIGHT)

    html_elem = driver.find_element(By.TAG_NAME, 'html')
    html_elem.send_keys(Keys.DOWN)

    html_elem = driver.find_element(By.TAG_NAME, 'html')
    html_elem.send_keys(Keys.LEFT)


def click_restart_button(driver):
    """Clicks the retry button."""
    # Need to press the New game button in anchor tag with class of restart-button.
    try:
        restart_button = driver.find_element(By.CLASS_NAME, 'restart-button')
        restart_button.click()
    except NoSuchElementException:
        print("Cannot find element with the classs of 'restart-button'", flush=True)


if __name__ == '__main__':
    game_url = os.getenv('GAME_URL', 'https://play2048.co')
    loop = os.getenv('LOOP', True)

    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    browser = webdriver.Remote('http://selenium_chrome:4444/wd/hub', options=options)
    browser.get(game_url)

    while True:
        while not is_game_over(browser):
            al_strategy(browser)

        if loop:
            click_restart_button(browser)
