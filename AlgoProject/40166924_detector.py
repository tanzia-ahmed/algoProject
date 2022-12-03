import string
import re

hash_table = {"one":[],"two":[]}
nGram = 5
filters = {'he', 'no', 'do', 'wasn', 'between', 't', 'm', 'was', 'with', 'other', 'down', 'above', 'does', 'they', 'but', 's',
                         "you've", 'those', "hasn't", 'of', 'were', 'doing', 'when', 'too', 'before', 'more', 'ain', 'won', 'a', 'nor', 'this',
                         "mightn't", 'has', 'have', 'through', 'ourselves', 'if', 'or', "haven't", 'by', 'we', 'these', 'against', 'the', 'should',
                         'its', "shan't", 'now', 'me', 'haven', 'then', 'am', 'into', 'is', 'll', 'couldn', 'once', 'not', "mustn't", "she's", 'while',
                         'under', "you'd", 'about', 'an', "that'll", 'you', 'theirs', "wouldn't", 're', "weren't", 'her', 'from', "it's", 'ours', 'how',
                         'as', 'there', 'which', 'most', 'myself', 'i', "you're", 'own', 'very', "didn't", 'needn', 'shan', "needn't", 'yourself', 'such',
                         'what', 'to', 'who', 'ma', 'she', 'all', "hadn't", 'on', 'and', 'where', "doesn't", 'their', 'mustn', 'don', "couldn't", 'herself',
                         'up', 'your', 'over', 'having', 'again', 'each', 'had', 'shouldn', 'both', 'hadn', 'his', 'being', 'doesn', 'because', 'mightn', 'my',
                         "you'll", 'itself', "isn't", 'himself', 'are', "don't", 'some', 'wouldn', 'only', 'in', 'any', 'at', 'whom', 'that', 'yours', 'further',
                         'after', 'yourselves', 'be', 'will', "should've", "won't", 'weren', 'them', 'themselves', 'few', 'did', 'aren', "aren't", 'o', 'hasn', 'so',
                         'until', 'off', 'can', 'here', 'didn', 'than', 'during', 'been', 'why', 'same', 'isn', 'below', 'd', 've', 'out', 'hers', "shouldn't", "wasn't",
                         'it', 'y', 'just', 'our', 'him', 'for'}

class hash_class:
    def __init__(self, cnt, ngram):
        self.ngram = ngram
        self.cnt = cnt
        self.char_size = 26
        self.start = 0
        self.end = 0
        self.num = 5807
        self.h = self.hashFunction(cnt, ngram)

#ord returns the unicode of a character. We subtract 96 to get the alphabetical ordering value of the letter. ex: a is 97, b is 98. 97-96 = 1, i.e. the placement of a in alphabets.
    def hashFunction(self, cnt, ngram):
        h = 0
        for i in range(0, ngram):
            h = h + (ord(cnt[i]) - 96) * (self.char_size ** (ngram - i - 1)) % self.num

        self.s = 0
        self.e = ngram

        return h
    def nextInx(self):
        if self.e <= len(self.cnt) - 1:
            self.h -= (ord(self.cnt[self.s]) - 96) * self.char_size ** (self.ngram - 1)
            self.h *= self.char_size
            self.h += ord(self.cnt[self.e]) - 96
            self.h %= self.num
            self.s += 1
            self.e += 1
            return True
        return False

def RabKarp (final1, final2, FILE1_TEXT, FILE2_TEXT):

    mappinng(final1, FILE1_TEXT,"one")
    mappinng(final2, FILE2_TEXT,"two")
    rate = getRate(hash_table)
    return rate

def mappinng(file_list, file, hash_index):

    content_joined = "".join(file_list)
    content_joined = hash_class(content_joined, nGram)
    for _ in range(len(file) - nGram + 1):
        hash_table[hash_index].append(content_joined.h)
        if content_joined.nextInx() == False:
            break


def getRate(hash_table):

    factor = len(list(set(hash_table["one"]) & set(hash_table["two"])))
    rate = (float(2 * factor) / (len(hash_table["one"]) + len(hash_table["two"]))) * 100

    return rate



if __name__ == '__main__':
    # getting files
    file1 = open("1.txt", "r", encoding="utf8")
    FILE1_TEXT = file1.read()
    file2 = open("2.txt", "r", encoding="utf8")
    FILE2_TEXT = file2.read()

    # splitting file contents into list
    list_1 = FILE1_TEXT.split()
    list_2 = FILE2_TEXT.split()

    #  lowering cases, removing punctuations
    for i in range(len(list_1)):
        list_1[i] = list_1[i].lower()
        list_1[i] = list_1[i].translate(str.maketrans("", "", string.punctuation))
        list_1[i] = list_1[i].strip("\“")
        list_1[i] = list_1[i].strip("\”")
        list_1[i] = list_1[i].replace("’","")

    for i in range(len(list_2)):
        list_2[i] = list_2[i].lower()
        list_2[i] = list_2[i].translate(str.maketrans("", "", string.punctuation))
        list_2[i] = list_2[i].strip("\“")
        list_2[i] = list_2[i].strip("\”")
        list_2[i] = list_2[i].replace("’","")

    # #  removing stopwords
    list_1 = [word for word in list_1 if word.lower() not in filters]
    list_2 = [word for word in list_2 if word.lower() not in filters]


    #  stemming words by prefixes and suffixes
    final1 = list()
    for i in list_1:
        j = re.sub(r'less|ship|ing|les|ly|es|s|ora|ous|ble|tional|ization|ism|tive|ness|ent|ment|ize|ive|ici|al', '', i)
        final1.append(j)
    final2 = list()
    for i in list_2:
        j = re.sub(r'less|ship|ing|les|ly|es|s|ora|ous|ble|tional|ization|ism|tive|ness|ent|ment|ize|ive|ici|al', '',i)
        final2.append(j)
    # #  ------------PRE-PROCESSING DONE-------------------

    rate = RabKarp(final1, final2, FILE1_TEXT, FILE2_TEXT)
    print(rate)

    if rate > 28.8:
        author = "(?:[A-Z][A-Za-z'`-]+)"
        etal = "(?:et al.?)"
        additional = "(?:,? (?:(?:and |& )?" + author + "|" + etal + "))"
        year_num = "(?:19|20)[0-9][0-9]"
        page_num = "(?:, p.? [0-9]+)?"  # Always optional
        year = "(?:, *" + year_num + page_num + "| *\(" + year_num + page_num + "\))"
        regex = "(" + author + additional + "*" + year + ")"

        # rx = re.compile(r"\([^()\d]*\d[^()]*\)")

        matches1 = re.findall(regex, FILE1_TEXT)
        matches2 = re.findall(regex, FILE2_TEXT)
        print(matches2)
        if len(matches2) > 0:
            print(0)
        else:
            print(1)
    else:
        print(0)

