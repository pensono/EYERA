
def first_duplicate(test, referenceParagraphs):
    # Use a really dumb metric where if two keywords match, it's a duplicate
    for paragraph in referenceParagraphs:
        if len(set.intersection(set(test['keywords']), set(paragraph['keywords']))) >= 2:
            return paragraph
    return None


def frankenarticle(articles):
    # Build our de duplicated article

    rejects = []
    # Start by just grabbing the content of the first one
    all_articles = articles
    dedup_article = all_articles[0]['paragraphs']

    for article in all_articles[1:]:
        for paragraph in article['paragraphs']:
            #  See if it's a duplicatePYU
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

    return "\n".join([paragraph['text'] for paragraph in dedup_article])
#    print("Article:")
#    for paragraph in dedup_article:
#        print(paragraph['text'])
#
#    print("")
#    print("Rejects:")
#    for reject in rejects:
#        print(reject['reject']['text'] + " ==== Matched with: " + reject['matched_with']['text'])

