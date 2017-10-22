from glob import glob


def get_lines_no_blanks(filename):
    return [line.strip() for line in open(filename, 'r', encoding='utf8').readlines() if len(line.strip()) > 0]


def get_articles():
    articles = []
    for file in glob("data/*.txt"):
        base = file.split('.')[0]
        print("Reading from " + file)
        paragraphs = get_lines_no_blanks(base + ".txt")
        keywords = get_lines_no_blanks(base + '.keywords')

        articles.append([{'text': z[0], 'keywords': z[1].split(" ")} for z in zip(paragraphs, keywords)])
    return articles


def first_duplicate(test, reference):
    # Use a really dumb metric where if two keywords match, it's a duplicate
    for paragraph in reference:
        if len(set.intersection(set(test['keywords']), set(paragraph['keywords']))) >= 2:
            return paragraph
    return None

# Build our de duplicated article

rejects = []
# Start by just grabbing the content of the first one
all_articles = get_articles()
dedup_article = all_articles[0]

for article in all_articles[1:]:
    for paragraph in article:
        #  See if it's a duplicate
        dup = first_duplicate(paragraph, dedup_article)
        if dup is None:
            dedup_article.append(paragraph)
        else:
            # reject the shortest one.
            index = dedup_article.index(dup)
            use = dup if len(dup['text']) > len(paragraph['text']) else paragraph
            reject = paragraph if len(dup['text']) > len(paragraph['text']) else dup
            dedup_article[index] = use
            rejects.append({'reject': reject, 'matched_with': use})

print("Article:")
for paragraph in dedup_article:
    print(paragraph['text'])

print("")
print("Rejects:")
for reject in rejects:
    print(reject['reject']['text'] + " ==== Matched with: " + reject['matched_with']['text'])

