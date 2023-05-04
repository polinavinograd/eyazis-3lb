import nltk
import pymorphy2
from ruwordnet import RuWordNet

# import ssl
#
# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#     ssl._create_default_https_context = _create_unverified_https_context
#
# nltk.download('wordnet')
PATH_TO_RUWORDNET = '../ruwordnet-2021.db'

wn = RuWordNet(filename_or_session=PATH_TO_RUWORDNET)


def create_dict(word):
    word_dict = {}
    antonyms = []
    synonyms = []
    hyponyms = []
    hypernyms = []
    holonyms = []  # получаем холонимы
    try:
        for i in wn[word]:
            for a in i.synset.antonyms:
                antonyms.append(a.title)
        for i in wn[word]:
            for s in i.synset.pos_synonyms:
                synonyms.append(s.title)

        for i in wn[word]:
            for h in i.synset.hyponyms:
                hyponyms.append(h.title)

        for i in wn[word]:
            for h in i.synset.hypernyms:
                hypernyms.append(h.title)

        for i in wn[word]:
            for h in i.synset.holonyms:
                holonyms.append(h.title)
        word_dict['word'] = word
        word_dict['Syn'] = ", ".join(synonyms)
        word_dict['Ant'] = ", ".join(antonyms)
        word_dict['Hypon'] = ", ".join(hyponyms)
        word_dict['Hyper'] = ", ".join(hypernyms)
        word_dict['Holon'] = ", ".join(holonyms)
        return word_dict
    except Exception as e:
        print(e)


def analize(text):
    res_list = list()
    tokens_word = nltk.word_tokenize(text)
    for t in tokens_word:
        morph = pymorphy2.MorphAnalyzer()
        word = morph.parse(t)[0].normal_form
        res = create_dict(word)
        if res:
            res_list.append(res)
    return res_list


if __name__ == '__main__':
    sentence = 'Белый кот на издание огромной скорости проскочил мимо чёрной собаки.'
    main_dict = analize(sentence)
    for i in main_dict:
        print(i)

