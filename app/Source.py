import math
import re

class Source(object):
    name = ""
    reliability = 0
    polarization = 0
    POLARIZATION_RANKINGS = ["Left Bias", "Left-Center Bias", "Least Bias", "Right-Center Bias", "Right Bias"]
    highest = False
    lowest = False

    def __init__(self, url, reliability, bias):
        self.name = self.parse_url(url)
        self.reliability = reliability
        self.polarization = self.POLARIZATION_RANKINGS.index(bias)

    #for testing purposes only
    def __str__(self):
        return str(self.polarization)

    def parse_url(self, url):
        result = re.match(r"https?://([\w.]+?)/", url).group(1)
        return result.replace("www.", "")





