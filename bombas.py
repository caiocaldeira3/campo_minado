class bomb:
    
    def flag(self):
        if self.show == '<|':
            self.flagged = 0
            self.show = '--'
        elif self.show != '--':
            print('Você não pode marcar minas já clicadas!')
        else:
            self.flagged = 1
            self.show = '<|'

    def on_click(self, minefield):
        if self.flagged == 1:
            return 1
        if self.active:
            self.show = self.value
            return -1
        else:
            if self.show != '--':
                return
            self.show = self.value
            if self.value == 0:
                try:
                    bomb.on_click(minefield[self.lin+1][self.col+1], minefield)
                except:
                    pass
                try:
                    bomb.on_click(minefield[self.lin+1][self.col], minefield)
                except:
                    pass
                try:
                    bomb.on_click(minefield[self.lin][self.col+1], minefield)
                except:
                    pass

                if self.lin - 1 >= 0:
                    try:
                        bomb.on_click(minefield[self.lin-1][self.col+1], minefield)
                    except:
                        pass
                    try:
                        bomb.on_click(minefield[self.lin-1][self.col], minefield)
                    except:
                        pass
                if self.col - 1 >= 0:
                    try:
                        bomb.on_click(minefield[self.lin+1][self.col-1], minefield)
                    except:
                        pass
                    try:
                        bomb.on_click(minefield[self.lin][self.col-1], minefield)
                    except:
                        pass
                if self.col - 1 >= 0 and self.lin - 1 >= 0:
                    try:
                        bomb.on_click(minefield[self.lin-1][self.col-1], minefield)
                    except:
                        pass

        return 1

class active_bomb(bomb):
    def __init__(self):
        self.active = 1
        self.value = '*'
        self.show = '--'
        self.flagged = 0

class inactive_bomb(bomb):
    def __init__(self, lin ,col):
        self.active = 0
        self.show = '--'
        self.lin = lin
        self.col = col
        self.flagged = 0

    def calc_value(self, minefield):
        lin, col = self.lin, self.col
        self.value = 0
        if lin - 1 >= 0:
            try:
                if minefield[lin-1][col].active == 1:
                    self.value += 1
            except:
                pass
            try:
                if minefield[lin-1][col+1].active == 1:
                    self.value += 1
            except:
                pass
        if col - 1 >= 0:
            try:
                if minefield[lin][col-1].active == 1:
                    self.value += 1
            except:
                pass
            try:
                if minefield[lin+1][col-1].active == 1:
                    self.value += 1
            except:
                pass
        if lin - 1 >= 0 and col - 1 >= 0:
            try:
                if minefield[lin-1][col-1].active == 1:
                    self.value += 1
            except:
                pass

        try:
            if minefield[lin+1][col+1].active == 1:
                self.value += 1
        except:
            pass
        try:
            if minefield[lin+1][col].active == 1:
                self.value += 1
        except:
            pass
        try:
            if minefield[lin][col+1].active == 1:
                self.value += 1
        except:
            pass
