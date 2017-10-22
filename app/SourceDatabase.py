import math


class SourceDatabase(object):
    sources = []

    def __init__(self, source):
        self.sources.append(source)

    def get_polarization(self, name):
        for x in range(0, len(self.sources)):
            if self.sources[x].name == name:
                return self.sources[x].polarization

    #returns tuple of most opposite sources; highest (most right) source first and lowest (most left) sources second.
    def find_most_different(self):
        return self.find_max(), self.find_min()

    def find_max(self):
        max = self.sources[0]
        for x in range(1, len(self.sources)):
            if self.sources[x].polarization > max.polarization:
                max = self.sources[x]
        max.highest = True
        return max

    def find_min(self):
        min = self.sources[0]
        for x in range (1, len(self.sources)):
            if self.sources[x].polarization < min.polarization:
                min = self.sources[x]
        min.lowest = True
        return min






