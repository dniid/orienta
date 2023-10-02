from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


class MinesweeperSolver:
    def __init__(self, h, w, m, driver):
        self.driver = driver
        self.dx = [1, 1, 1, -1, -1, -1, 0, 0]
        self.dy = [-1, 1, 0, -1, 1, 0, -1, 1]
        self.height = h
        self.width = w
        self.mines = m
        self.state = [[-2 for i in range(w + 1)] for j in range(h + 1)]
        self.safe_q = set()
        self.safe_b = set()
        self.revealed = set()
        self.unknowns = set()
        self.bombs = set()

        for i in range(1, h + 1):
            for j in range(1, w + 1):
                self.unknowns.add((i, j))

    def get_id(self, cell):
        return str(cell[0]) + '_' + str(cell[1])

    def is_inside(self, cell):
        return 1 <= cell[0] <= self.height and 1 <= cell[1] <= self.width

    def get_more(self):
        ret = 0
        if True:
            for cell in self.revealed:
                num = [0, 0, 0]
                maybe = []
                for k in range(8):
                    x, y = cell[0] + self.dx[k], cell[1] + self.dy[k]
                    if self.is_inside((x, y)):
                        num[2] += 1
                        if self.state[x][y] == -1:
                            num[1] += 1
                        elif self.state[x][y] != -2:
                            num[0] += 1
                        elif self.state[x][y] == -2:
                            maybe.append((x, y))

                if num[1] == self.state[cell[0]][cell[1]]:
                    for xcell in maybe:
                        self.safe_q.add(xcell)
                        ret += 1
                elif len(maybe) > 0 and self.state[cell[0]][cell[1]] - num[1] == len(maybe):
                    for xcell in maybe:
                        self.safe_b.add(xcell)
                        self.state[xcell[0]][xcell[1]] = -1
                        ret += 1

        if ret == 0:
          self.safe_q.add(self.unknowns.pop())

    def next_safe(self):
        return self.safe_q.pop()

    def next_bomb(self):
        return self.safe_b.pop()

    def parse_cell_state(self, cell, cell_state):
        if 'bombflagged' in cell_state:
            return -1
        if 'blank' in cell_state:
            return -2
        return int(cell_state[-1])

    def update_state(self):
        out = set()
        for cell in self.unknowns:
            pcell = self.driver.find_element(By.ID, self.get_id(cell))
            cell_class = pcell.get_attribute('class')
            self.state[cell[0]][cell[1]] = self.parse_cell_state(cell, cell_class)
            if self.state[cell[0]][cell[1]] != -2:
                out.add(cell)
        self.unknowns -= out
        self.revealed |= out

    def click_cell(self, cell, left_click=True):
        pcell = self.driver.find_element(By.ID, self.get_id(cell))
        if left_click:
            pcell.click()
        else:
            self.bombs.add(cell)
            ActionChains(self.driver).move_to_element(pcell).context_click(pcell).perform()

    def mouse_feed(self, cycle):
        print ('At cycle #', cycle)
        if len(self.revealed) == self.height * self.width:
            return
        self.get_more()
        while len(self.safe_q):
            cell = self.next_safe()
            self.click_cell(cell)
        while len(self.safe_b):
            cell = self.next_bomb()
            self.click_cell(cell, False)
        self.update_state()
        self.mouse_feed(cycle + 1)

    def start_playing(self, game_url):
        self.driver.get(game_url)
        self.driver.implicitly_wait(5)
        self.mouse_feed(0)
