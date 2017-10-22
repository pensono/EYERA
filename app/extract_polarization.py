from app.Source import Source
from app.SourceDatabase import SourceDatabase


class ExtractPolarization:
    def __init__(self):
        database = self.make_sources()
        result = database.find_most_different()

    def make_sources(self):
        nytimes = Source("https://www.nytimes.com/2017/10/20/health/social-media-fake-news.html", 0, "Left-Center Bias")
        americanthinker = Source("http://www.americanthinker.com/articles/2015/02/obama_and_the_muslim_gang_sign.html", 0, "Right Bias")
        aljazeera = Source("http://www.aljazeera.com/news/2017/10/trump-turbulent-week-considered-171021062558434.html", 0, "Left-Center Bias")
        watimes = Source("http://www.washingtontimes.com/news/2017/oct/18/vladimir-putins-rage-triggered-by-president-obamas/", 0, "Right-Center Bias")
        crooksandliars = Source("http://crooksandliars.com/2017/10/mississippi-school-named-obama-and-fox", 0, "Left Bias")
        bbc = Source("http://www.bbc.com/news/world-us-canada-41689805", 0, "Left-Center Bias")
        atlantic = Source("https://www.theatlantic.com/international/archive/2017/10/trump-obama-foreign-policy-iran/542727/?silverid=MzYwODg4MTgzNTQyS0", 0, "Left-Center Bias")

        database = SourceDatabase(nytimes)
        database.sources.append(americanthinker)
        database.sources.append(aljazeera)
        database.sources.append(watimes)
        database.sources.append(crooksandliars)
        database.sources.append(bbc)
        database.sources.append(atlantic)

        return database

t = ExtractPolarization()



