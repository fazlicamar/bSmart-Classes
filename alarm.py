class Alarm:
    def __init__(self, state):
        self.state = True

    def changeState(self):
        if self.state == False:
            return("Your alarm just went off, check it")