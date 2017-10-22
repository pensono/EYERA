import math

class Source(object):
    name = ""
    reliability = 0
    polarization = 0
    POLARIZATION_RANKINGS = ["Left Bias", "Left-Center Bias", "Least Bias", "Right-Center Bias", "Right Bias"]
    highest = False
    lowest = False

    def __init__(self, name, reliability, bias):
        self.name = name
        self.reliability = reliability
        self.polarization = self.POLARIZATION_RANKINGS.index(bias)

    #for testing purposes only
    def __str__(self):
        return str(self.polarization)




