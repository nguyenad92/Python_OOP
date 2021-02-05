class Animal():
    def __init__(self,):
        self.name = name 
        self.height 
        self.weight 
        self.sound

    def setName(self, name):
        self.name = name

    def setWeight(self, newWeight):
        if newWeight > 0:
            self.weight = newWeight
        else:
            print("Weight must be bigger than 0")

    def getWeight(self):
        return self.weight

    def setSound(self, sound):
        self.sound = sound
    def getSound(self):
        return self.sound
