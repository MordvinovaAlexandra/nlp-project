import pymorphy2

def get_nouns(words: list[str]) -> list[str]:
    parser = pymorphy2.MorphAnalyzer()
    
    return [word for word in words if parser.parse(word)[0].tag.POS == 'NOUN']
    # for word in words:
    #     tag = parser.parse(word)[0].tag.POS
    #     print(pos)
    

# get_nouns(['Тотошка','спросила', 'домик', 'гуляют'])

def normalize(words: list[str]) -> list[str]:
    parser = pymorphy2.MorphAnalyzer()
    return [parser.parse(word)[0].normal_form for word in words]
