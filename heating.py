class Heating:
    
    def __init__(self, temp, state):
        self.temp = 0.0 
        self.state = False

    def setTemp(self, newTemp):
        self.temp = newTemp
    
    def setState(self, newTemp):
        if newTemp > 20:
            self.state = True
    

    