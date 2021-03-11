class Light:
    def __init__(self):
        self.state = False #indicates if the light is turned on or off
        self.brightness  = 0.0 #indicates brightness level of a light
        self.powerMeter = 0.0 #checks power consumption


    def getPowerConsumption(self): #returns power consumption
        return float(self.powerMeter)


    def turnOn(self):
        self.state = True

    def turnOff(self):
        self.state = False

    def getState(self):
        return self.state
 
