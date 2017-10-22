import re

def summarizer(article):
    summary = "";
    pattern = re.compile("[^\w\s']")  #removes non-word, non-white space characters
    for paragraphDict in article['paragraphs']:
        paragraph = paragraphDict['text'].split(".")
        keyWords = paragraphDict['keywords']

        key_word_counter = {}
        for sentence in paragraph:
            key_word_counter[sentence] = 0

            pattern.sub('', sentence)
            sentenceArr = sentence.split(" ")

            for word in sentenceArr:
                if word in keyWords:
                    key_word_counter[sentence] += 1

        best_word = ""
        key_count = 0
        for word in key_word_counter:
            if key_word_counter[word] > key_count:
                key_count = key_word_counter[word]
                best_word = word

        summary += best_word + ". "

    return summary

#this is a test, this is a test
if __name__ == "__main__":
    content = {'url':'', 'paragraphs': [
            {'text': "Hello this is a test file. This is a better sentence. Ya ya hello. This is better better better sentence.",
             'keywords': ["better", "sentence"]}, {'text': "New new paragraph that is what I am. Lame old paragraph is not what I am.",
            'keywords': ["new", "paragraph"]}
        ]}

    print(summarizer(content))


