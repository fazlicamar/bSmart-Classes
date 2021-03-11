class Sensor:

    def __init__(self, state):
        self.state = False


class Smoke(Sensor):

    def ifActive(self, sensor):
        if sensor == True:
            return("There seems to be a problem with your smoke sensor, check it out")

class Rain(Sensor):

    def ifActive(self, sensor):
        if sensor == True:
            return("There seems to be a problem, you left a window open and there is rain")


class GasLeak(Sensor):

    def ifActive(self, sensor):
        if sensor == True:
            return("There seems to be a problem with your gas leak sensor, check it out")
