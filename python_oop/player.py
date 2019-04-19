class Player:
    def __init__(self):
        self.fname = ""
        self.lname = ""
        self.number = ""


class Player2:
    def __init__(self, fname, lname, number):
        self.fname = fname
        self.lname = lname
        self.number = number


if __name__ == '__main__':
    p1 = Player()
    p1.fname = "Loris"
    p1.lname = "Karius"
    p1.number = 1
