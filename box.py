class Box():
    def __init__(self, width, height, length):
        self.width = width
        self.height = height
        self.length = length
        self.volume

    def getVolume(self):
        self.volume = self.width*self.height*self.length
        return self.volume

    def __str__(self):
        return "Box with width = " + str(self.width) + " ,height = " + str(self.height) + " ,length = " + str(self.length)

