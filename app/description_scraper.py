import xlrd
import collections
# import nltk
import json

# We need a dictionary to store a list of words for the description to each position
# Assignment ID: [list of words in description]
def scraper():
    book = xlrd.open_workbook(filename= "position_descriptions.xlsx")
    sheet = book.sheet_by_index(0)
    list_of_all_words = []
    assignments = dict()
    words_to_remove = ["act","as","and","to","the","of","with","in","for","a","on","as","be","or","will","-","is","applications","requirements","client","experience","that","issues","meet",
    "work","provide","within"]
    for rows in range(1, sheet.nrows):
        value = (sheet.cell_value(rows,16)+" "+sheet.cell_value(rows,15)+" "+sheet.cell_value(rows,25)+" "+sheet.cell_value(rows,26)+" "+sheet.cell_value(rows,34)).lower()
        value = value.replace(",", "")
        value = value.replace(".", "")
        words = value.split()
        if(len(words) <= 1):
            continue
        # print("Words before:")
        # print(words)
        for word in words_to_remove:
            words = list(filter(lambda a: a != word, words))
        # print("\nWords after:")
        # print(words)
        # input()
        descript_words = []
        for i in words:
            list_of_all_words.append(i)
            descript_words.append(i)
        assignments[sheet.cell_value(rows, 0)] = {"words":descript_words,
                                                  "career_level_from":sheet.cell_value(rows,23),
                                                  "career_level_to":sheet.cell_value(rows,24)}

    wordcount = collections.Counter(list_of_all_words)
    most_common = wordcount.most_common(10)
    print("Most common words in descriptions: ",most_common)


    # for i in assignments.keys():
    #     input()
    #     print(assignments[i])
    return assignments
