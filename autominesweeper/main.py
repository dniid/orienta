import os
from selenium import webdriver
from solver import MinesweeperSolver


if __name__ == '__main__':
    game_url = os.getenv('GAME_URL', 'http://www.minesweeperonline.com')

    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    browser = webdriver.Remote('http://selenium_chrome:4444/wd/hub', options=options)
    solver = MinesweeperSolver(16, 30, 99, browser)
    solver.start_playing(game_url)
