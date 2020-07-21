from pdfminer.high_level import extract_text
import collections

def scraper(resume):
    list_of_all_words = []
    words_to_remove = ["act","as","and","to","the","of","with","in","for","a","on","as","be","or","will","-","is","applications","requirements","client","experience","that","issues","meet",
    "work","provide","within","an","by","into","up","new","other","may","between","high","-","through","using","spring","hours","across","from","candidate","needs","part","ensure","effort","major","helped","4","life","–","schedule","state","utlizing"]
    words = extract_text(resume).lower().replace(",", "").replace(".", "").replace('•',"").split()
    count = collections.Counter(words)
    # print(collections.counter(extract_text('resume.pdf')))
    # print(count)
    most_common = count.most_common(10)
    # print("Words before:")
    # print(words)
    for word in words_to_remove:
        words = list(filter(lambda a: a != word, words))
    # print("\nWords after:")
    # print(words)
    return words

if __name__ == '__main__':
    scraper()


# intersection of the non-filler words in the resume with non-filler words in each description.
# higher the count in the intersection the higher the matching is
