import re
from counter import count_words__counter
from stopwords import without_stopwords
from morph import get_nouns, normalize

def load(path: str, encoding: str = 'utf-8') -> str:
    with open(path, encoding =encoding, errors = 'ignore') as f:
        data = f.read()
    return data

# def preprocess(text: str) -> str:
#     # добавить ентити рекогнишн
#     return text

def tokenize(text: str) -> list[str]:
   return re.findall(r'\w{2,}', text)


if __name__ == '__main__':
    text = load('./TEXT/wizard_oz.txt', encoding = 'cp1251')
    # text = preprocess(text)
    words = without_stopwords(tokenize(text))
    nouns = [normalize(word) for word in get_nouns(words)]
    # print(words[:20])
    # print(count_words(words))
    # print(count_words__count(words))
    print(count_words__counter(nouns))