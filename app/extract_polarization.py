from app.Source import Source
from app.SourceDatabase import SourceDatabase


class ExtractPolarization:
    def __init__(self):
        database = self.make_sources()
        result = database.find_most_different()
        print(result[0])
        print(result[1])

    def make_sources(self):
        bbc = Source("BBC", 0, "Left-Center Bias")
        dw = Source("DW", 0, "Left-Center Bias")
        ft = Source("Financial Times", 0, "Least Bias")

        database = SourceDatabase(bbc)
        database.sources.append(dw)
        database.sources.append(ft)
        return database

t = ExtractPolarization()



