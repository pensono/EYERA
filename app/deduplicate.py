
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
                if len(dup['text']) > len(paragraph['text']):
                    rejects.append({'reject': paragraph, 'matched_with': dup})
                else:
                    dedup_article.remove(dup)
                    dedup_article.append(paragraph)
                    rejects.append({'reject': dup, 'matched_with': paragraph})

    return "\n".join([paragraph['text'] for paragraph in dedup_article[:15]])


if __name__ == '__main__':
    from app.related_articles import *
    from app.extract_keywords import *

    # Build our de duplicated article

    rejects = []
    # Start by just grabbing the content of the first one
    all_articles = get_related("trump border wall")
    for article in all_articles:
        keywords = keywords_from_article(article)

        for z in zip(keywords, article['paragraphs']):
            z[1]['keywords'] = z[0]  # Just think about it a little

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
                if len(dup['text']) > len(paragraph['text']):
                    rejects.append({'reject': paragraph, 'matched_with': dup})
                else:
                    dedup_article.remove(dup)
                    dedup_article.append(paragraph)
                    rejects.append({'reject': dup, 'matched_with': paragraph})

    print("Article:")
    for paragraph in dedup_article[:15]:
        print(paragraph['text'])

    print("")
    print("Rejects:")
    for reject in rejects:
        print(reject['reject']['text'] + " ==== Matched with: " + reject['matched_with']['text'])

