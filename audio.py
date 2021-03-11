class Audio:
    def __init__(self, level, state):
        self.level = 0.0 #indicates the level of audio
        self.state = False #checks the state

    def setVolume(self, volume):
        self.level = volume #changes the volume which is inputed by the user

    def checkState(self):
        return self.state #returns if the speakers are on or off

