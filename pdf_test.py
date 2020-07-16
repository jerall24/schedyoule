from PyPDF2 import PdfFileReader
from PyPDF2.pdf import PageObject
from pdfminer.high_level import extract_text
import collections

def main():
    # input = PdfFileReader(open("resume.pdf", "rb"))
    #
    # print(input.getPage(0).extractText())
    # count = Counter()
    lst = extract_text("resume.pdf").replace("\n","").replace(".", "").replace(",","").replace('',"").split(" ")
    count = collections.Counter(lst)
    # print(collections.counter(extract_text('resume.pdf')))
    # print(count)
    most_common = count.most_common(10)
    print(most_common)

if __name__ == '__main__':
    main()


# intersection of the non-filler words in the resume with non-filler words in each description.
# higher the count in the intersection the higher the matching is 
