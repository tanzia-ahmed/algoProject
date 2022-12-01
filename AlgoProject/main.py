# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import string
import  re
from math import sqrt,acos,cos


# stopwords = ["0o", "0s", "3a", "3b", "3d", "6b", "6o", "a", "a1", "a2", "a3", "a4", "ab", "able", "about", "above", "abst", "ac", "accordance", "according", "accordingly", "across", "act", "actually", "ad", "added", "adj", "ae", "af", "affected", "affecting", "affects", "after", "afterwards", "ag", "again", "against", "ah", "ain", "ain't", "aj", "al", "all", "allow", "allows", "almost", "alone", "along", "already", "also", "although", "always", "am", "among", "amongst", "amoungst", "amount", "an", "and", "announce", "another", "any", "anybody", "anyhow", "anymore", "anyone", "anything", "anyway", "anyways", "anywhere", "ao", "ap", "apart", "apparently", "appear", "appreciate", "appropriate", "approximately", "ar", "are", "aren", "arent", "aren't", "arise", "around", "as", "a's", "aside", "ask", "asking", "associated", "at", "au", "auth", "av", "available", "aw", "away", "awfully", "ax", "ay", "az", "b", "b1", "b2", "b3", "ba", "back", "bc", "bd", "be", "became", "because", "become", "becomes", "becoming", "been", "before", "beforehand", "begin", "beginning", "beginnings", "begins", "behind", "being", "believe", "below", "beside", "besides", "best", "better", "between", "beyond", "bi", "bill", "biol", "bj", "bk", "bl", "bn", "both", "bottom", "bp", "br", "brief", "briefly", "bs", "bt", "bu", "but", "bx", "by", "c", "c1", "c2", "c3", "ca", "call", "came", "can", "cannot", "cant", "can't", "cause", "causes", "cc", "cd", "ce", "certain", "certainly", "cf", "cg", "ch", "changes", "ci", "cit", "cj", "cl", "clearly", "cm", "c'mon", "cn", "co", "com", "come", "comes", "con", "concerning", "consequently", "consider", "considering", "contain", "containing", "contains", "corresponding", "could", "couldn", "couldnt", "couldn't", "course", "cp", "cq", "cr", "cry", "cs", "c's", "ct", "cu", "currently", "cv", "cx", "cy", "cz", "d", "d2", "da", "date", "dc", "dd", "de", "definitely", "describe", "described", "despite", "detail", "df", "di", "did", "didn", "didn't", "different", "dj", "dk", "dl", "do", "does", "doesn", "doesn't", "doing", "don", "done", "don't", "down", "downwards", "dp", "dr", "ds", "dt", "du", "due", "during", "dx", "dy", "e", "e2", "e3", "ea", "each", "ec", "ed", "edu", "ee", "ef", "effect", "eg", "ei", "eight", "eighty", "either", "ej", "el", "eleven", "else", "elsewhere", "em", "empty", "en", "end", "ending", "enough", "entirely", "eo", "ep", "eq", "er", "es", "especially", "est", "et", "et-al", "etc", "eu", "ev", "even", "ever", "every", "everybody", "everyone", "everything", "everywhere", "ex", "exactly", "example", "except", "ey", "f", "f2", "fa", "far", "fc", "few", "ff", "fi", "fifteen", "fifth", "fify", "fill", "find", "fire", "first", "five", "fix", "fj", "fl", "fn", "fo", "followed", "following", "follows", "for", "former", "formerly", "forth", "forty", "found", "four", "fr", "from", "front", "fs", "ft", "fu", "full", "further", "furthermore", "fy", "g", "ga", "gave", "ge", "get", "gets", "getting", "gi", "give", "given", "gives", "giving", "gj", "gl", "go", "goes", "going", "gone", "got", "gotten", "gr", "greetings", "gs", "gy", "h", "h2", "h3", "had", "hadn", "hadn't", "happens", "hardly", "has", "hasn", "hasnt", "hasn't", "have", "haven", "haven't", "having", "he", "hed", "he'd", "he'll", "hello", "help", "hence", "her", "here", "hereafter", "hereby", "herein", "heres", "here's", "hereupon", "hers", "herself", "hes", "he's", "hh", "hi", "hid", "him", "himself", "his", "hither", "hj", "ho", "home", "hopefully", "how", "howbeit", "however", "how's", "hr", "hs", "http", "hu", "hundred", "hy", "i", "i2", "i3", "i4", "i6", "i7", "i8", "ia", "ib", "ibid", "ic", "id", "i'd", "ie", "if", "ig", "ignored", "ih", "ii", "ij", "il", "i'll", "im", "i'm", "immediate", "immediately", "importance", "important", "in", "inasmuch", "inc", "indeed", "index", "indicate", "indicated", "indicates", "information", "inner", "insofar", "instead", "interest", "into", "invention", "inward", "io", "ip", "iq", "ir", "is", "isn", "isn't", "it", "itd", "it'd", "it'll", "its", "it's", "itself", "iv", "i've", "ix", "iy", "iz", "j", "jj", "jr", "js", "jt", "ju", "just", "k", "ke", "keep", "keeps", "kept", "kg", "kj", "km", "know", "known", "knows", "ko", "l", "l2", "la", "largely", "last", "lately", "later", "latter", "latterly", "lb", "lc", "le", "least", "les", "less", "lest", "let", "lets", "let's", "lf", "like", "liked", "likely", "line", "little", "lj", "ll", "ll", "ln", "lo", "look", "looking", "looks", "los", "lr", "ls", "lt", "ltd", "m", "m2", "ma", "made", "mainly", "make", "makes", "many", "may", "maybe", "me", "mean", "means", "meantime", "meanwhile", "merely", "mg", "might", "mightn", "mightn't", "mill", "million", "mine", "miss", "ml", "mn", "mo", "more", "moreover", "most", "mostly", "move", "mr", "mrs", "ms", "mt", "mu", "much", "mug", "must", "mustn", "mustn't", "my", "myself", "n", "n2", "na", "name", "namely", "nay", "nc", "nd", "ne", "near", "nearly", "necessarily", "necessary", "need", "needn", "needn't", "needs", "neither", "never", "nevertheless", "new", "next", "ng", "ni", "nine", "ninety", "nj", "nl", "nn", "no", "nobody", "non", "none", "nonetheless", "noone", "nor", "normally", "nos", "not", "noted", "nothing", "novel", "now", "nowhere", "nr", "ns", "nt", "ny", "o", "oa", "ob", "obtain", "obtained", "obviously", "oc", "od", "of", "off", "often", "og", "oh", "oi", "oj", "ok", "okay", "ol", "old", "om", "omitted", "on", "once", "one", "ones", "only", "onto", "oo", "op", "oq", "or", "ord", "os", "ot", "other", "others", "otherwise", "ou", "ought", "our", "ours", "ourselves", "out", "outside", "over", "overall", "ow", "owing", "own", "ox", "oz", "p", "p1", "p2", "p3", "page", "pagecount", "pages", "par", "part", "particular", "particularly", "pas", "past", "pc", "pd", "pe", "per", "perhaps", "pf", "ph", "pi", "pj", "pk", "pl", "placed", "please", "plus", "pm", "pn", "po", "poorly", "possible", "possibly", "potentially", "pp", "pq", "pr", "predominantly", "present", "presumably", "previously", "primarily", "probably", "promptly", "proud", "provides", "ps", "pt", "pu", "put", "py", "q", "qj", "qu", "que", "quickly", "quite", "qv", "r", "r2", "ra", "ran", "rather", "rc", "rd", "re", "readily", "really", "reasonably", "recent", "recently", "ref", "refs", "regarding", "regardless", "regards", "related", "relatively", "research", "research-articl", "respectively", "resulted", "resulting", "results", "rf", "rh", "ri", "right", "rj", "rl", "rm", "rn", "ro", "rq", "rr", "rs", "rt", "ru", "run", "rv", "ry", "s", "s2", "sa", "said", "same", "saw", "say", "saying", "says", "sc", "sd", "se", "sec", "second", "secondly", "section", "see", "seeing", "seem", "seemed", "seeming", "seems", "seen", "self", "selves", "sensible", "sent", "serious", "seriously", "seven", "several", "sf", "shall", "shan", "shan't", "she", "shed", "she'd", "she'll", "shes", "she's", "should", "shouldn", "shouldn't", "should've", "show", "showed", "shown", "showns", "shows", "si", "side", "significant", "significantly", "similar", "similarly", "since", "sincere", "six", "sixty", "sj", "sl", "slightly", "sm", "sn", "so", "some", "somebody", "somehow", "someone", "somethan", "something", "sometime", "sometimes", "somewhat", "somewhere", "soon", "sorry", "sp", "specifically", "specified", "specify", "specifying", "sq", "sr", "ss", "st", "still", "stop", "strongly", "sub", "substantially", "successfully", "such", "sufficiently", "suggest", "sup", "sure", "sy", "system", "sz", "t", "t1", "t2", "t3", "take", "taken", "taking", "tb", "tc", "td", "te", "tell", "ten", "tends", "tf", "th", "than", "thank", "thanks", "thanx", "that", "that'll", "thats", "that's", "that've", "the", "their", "theirs", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "thered", "therefore", "therein", "there'll", "thereof", "therere", "theres", "there's", "thereto", "thereupon", "there've", "these", "they", "theyd", "they'd", "they'll", "theyre", "they're", "they've", "thickv", "thin", "think", "third", "this", "thorough", "thoroughly", "those", "thou", "though", "thoughh", "thousand", "three", "throug", "through", "throughout", "thru", "thus", "ti", "til", "tip", "tj", "tl", "tm", "tn", "to", "together", "too", "took", "top", "toward", "towards", "tp", "tq", "tr", "tried", "tries", "truly", "try", "trying", "ts", "t's", "tt", "tv", "twelve", "twenty", "twice", "two", "tx", "u", "u201d", "ue", "ui", "uj", "uk", "um", "un", "under", "unfortunately", "unless", "unlike", "unlikely", "until", "unto", "uo", "up", "upon", "ups", "ur", "us", "use", "used", "useful", "usefully", "usefulness", "uses", "using", "usually", "ut", "v", "va", "value", "various", "vd", "ve", "ve", "very", "via", "viz", "vj", "vo", "vol", "vols", "volumtype", "vq", "vs", "vt", "vu", "w", "wa", "want", "wants", "was", "wasn", "wasnt", "wasn't", "way", "we", "wed", "we'd", "welcome", "well", "we'll", "well-b", "went", "were", "we're", "weren", "werent", "weren't", "we've", "what", "whatever", "what'll", "whats", "what's", "when", "whence", "whenever", "when's", "where", "whereafter", "whereas", "whereby", "wherein", "wheres", "where's", "whereupon", "wherever", "whether", "which", "while", "whim", "whither", "who", "whod", "whoever", "whole", "who'll", "whom", "whomever", "whos", "who's", "whose", "why", "why's", "wi", "widely", "will", "willing", "wish", "with", "within", "without", "wo", "won", "wonder", "wont", "won't", "words", "world", "would", "wouldn", "wouldnt", "wouldn't", "www", "x", "x1", "x2", "x3", "xf", "xi", "xj", "xk", "xl", "xn", "xo", "xs", "xt", "xv", "xx", "y", "y2", "yes", "yet", "yj", "yl", "you", "youd", "you'd", "you'll", "your", "youre", "you're", "yours", "yourself", "yourselves", "you've", "yr", "ys", "yt", "z", "zero", "zi", "zz",]
stopwords = {'he', 'no', 'do', 'wasn', 'between', 't', 'm', 'was', 'with', 'other', 'down', 'above', 'does', 'they',
                 'but', 's', "you've", 'those', "hasn't", 'of', 'were', 'doing', 'when', 'too', 'before', 'more', 'ain',
                 'won', 'a', 'nor', 'this', "mightn't", 'has', 'have', 'through', 'ourselves', 'if', 'or', "haven't",
                 'by', 'we', 'these', 'against', 'the', 'should', 'its', "shan't", 'now', 'me', 'haven', 'then', 'am',
                 'into', 'is', 'll', 'couldn', 'once', 'not', "mustn't", "she's", 'while', 'under', "you'd", 'about',
                 'an', "that'll", 'you', 'theirs', "wouldn't", 're', "weren't", 'her', 'from', "it's", 'ours', 'how',
                 'as', 'there', 'which', 'most', 'myself', 'i', "you're", 'own', 'very', "didn't", 'needn', 'shan',
                 "needn't", 'yourself', 'such', 'what', 'to', 'who', 'ma', 'she', 'all', "hadn't", 'on', 'and', 'where',
                 "doesn't", 'their', 'mustn', 'don', "couldn't", 'herself', 'up', 'your', 'over', 'having', 'again',
                 'each', 'had', 'shouldn', 'both', 'hadn', 'his', 'being', 'doesn', 'because', 'mightn', 'my', "you'll",
                 'itself', "isn't", 'himself', 'are', "don't", 'some', 'wouldn', 'only', 'in', 'any', 'at', 'whom',
                 'that', 'yours', 'further', 'after', 'yourselves', 'be', 'will', "should've", "won't", 'weren', 'them',
                 'themselves', 'few', 'did', 'aren', "aren't", 'o', 'hasn', 'so', 'until', 'off', 'can', 'here', 'didn',
                 'than', 'during', 'been', 'why', 'same', 'isn', 'below', 'd', 've', 'out', 'hers', "shouldn't",
                 "wasn't", 'it', 'y', 'just', 'our', 'him', 'for'}

# prefixes = ["dis","mis", "non", "pre", "pro", "re","un","in","il","ex", "im"]
# suffixes = ["less","ship","ing","les","ly","es","ed","y","s","ora","ous","ble","tional","tion","ization","ism","tive","ness","ent","ment","ize","ive","ici","al","de","re","able","ible","ful","est","er"]
# specialChars = ['!','"','#','$','%','&','(',')','*','+','/',':',';','<','=','>','@','[','\\',']','^','`','{','|','}','~','\t',"\“"]

def BoyerMorreHorspool(pattern, text):
    m = len(pattern)
    n = len(text)
    if m > n: return -1
    skip = []
    for k in range(256): skip.append(m)
    for k in range(m - 1):
        skip[ord(pattern[k])] = m - k - 1
    skip = tuple(skip)
    k = m - 1
    while k < n:
        j = m - 1;
        i = k
        while j >= 0 and text[i] == pattern[j]:
            j -= 1;
            i -= 1
        if j == -1: return i + 1
        k += skip[ord(text[k])]
    return -1
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # getting files
    file1 = open("1.txt", "r", encoding="utf8")
    FILE1_TEXT = file1.read()
    file2 = open("2.txt", "r", encoding="utf8")
    FILE2_TEXT = file2.read()

    # PRE- PROCESSING STARTS HERE
    #     removing punctuations
    FILE1_TEXT = FILE1_TEXT.translate(str.maketrans("","", string.punctuation))
    # FILE1_TEXT = FILE1_TEXT.strip("\“")
    # FILE1_TEXT = FILE1_TEXT.strip("\”")
    # FILE1_TEXT = FILE1_TEXT.strip("\’")
    # FILE2_TEXT = FILE2_TEXT.strip("\“")
    # FILE2_TEXT = FILE2_TEXT.strip("\”")
    # FILE2_TEXT = FILE2_TEXT.strip("\’")
    FILE2_TEXT = FILE2_TEXT.translate(str.maketrans("","", string.punctuation))



    list_1 = FILE1_TEXT.split()
    list_2 = FILE2_TEXT.split()



    #  lowering cases
    for i in range(len(list_1)):
        list_1[i] = list_1[i].lower()
        list_1[i] = list_1[i].strip("\“")
        list_1[i] = list_1[i].strip("\”")
        list_1[i] = list_1[i].replace("’","")

    for i in range(len(list_2)):
        list_2[i] = list_2[i].lower()
        list_2[i] = list_2[i].strip("\“")
        list_2[i] = list_2[i].strip("\”")
        list_2[i] = list_2[i].replace("’","")

    #  removing stopwords
    list_1 = [word for word in list_1 if word.lower() not in stopwords]
    list_2 = [word for word in list_2 if word.lower() not in stopwords]

    final1 = list()
    for i in list_1:
        word = re.sub(r'less|ship|ing|les|ly|es|s|ora|ous|ble|tional|ization|ism|tive|ness|ent|ment|ize|ive|ici|al', '', i)
        # word = re.sub(r'less|ship|ing|les|ly|es|ed|y|s|ora|ous|ble|tional|tion|ization|ism|tive|ness|ent|ment|ize|ive|ici|al|de|dis|mis|non|pre|pro|re|un|in|il|ex|im|able|ible|ful|est|er', '', i)
        final1.append(word)
    print(final1)
    final2 = list()
    for i in list_2:
        word = re.sub(r'less|ship|ing|les|ly|es|s|ora|ous|ble|tional|ization|ism|tive|ness|ent|ment|ize|ive|ici|al', '',
                      i)
        # word = re.sub(r'less|ship|ing|les|ly|es|ed|y|s|ora|ous|ble|tional|tion|ization|ism|tive|ness|ent|ment|ize|ive|ici|al|de|dis|mis|non|pre|pro|re|un|in|il|ex|im|able|ible|ful|est|er', '', i)
        final2.append(word)
    print(final2)


    # list_1_str = ' '.join(final1)
    # list_2_str = ' '.join(list_2)

    count = 0
    doc2_joined = ",".join(map(str, final2))
    print(doc2_joined)
    for i in final1:
        checkvar = 0
        checkvar = (BoyerMorreHorspool(str(i), doc2_joined))

        if checkvar > -1:
            count += 1

    print("The matches are: ", count)
    rate_plag = (2 * count) / (len(final1) + len(final2))
    print('\nThe rate of plagarisim ' + str(rate_plag))

    # dict_file1 = {}
    # dict_file2 = {}
    # for i in list_1:
    #     if i not in dict_file1:
    #         dict_file1[i.lower()] = 0
    #     dict_file1[i.lower()] += 1
    # for i in list_2:
    #     if i not in dict_file2:
    #         dict_file2[i.lower()] = 0
    #     dict_file2[i.lower()] += 1
    #
    # sum1 = sum(i * i for i in dict_file1.values())
    # sum2 = sum(i * i for i in dict_file2.values())
    # mod_fl1 = sqrt(sum1)
    # mod_fl2 = sqrt(sum2)
    # dotProduct = 0
    # for key in dict_file2:
    #     if key in dict_file1:
    #         dotProduct += dict_file1[key] * dict_file2[key]
    # distance = acos(dotProduct / int(mod_fl1 * mod_fl2))
    #
    #
    # print(distance)
    # print(list_2_str)




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
