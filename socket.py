class Socket:
    def __init__(self):
        self.state = False #indicates if the socket is in use
        self.usage = 0.0 #indicates the amount of power used

    
    def ifUsed(self):
        if self.usage != 0: 
            self.state = True
        return self.state
    
    

    
