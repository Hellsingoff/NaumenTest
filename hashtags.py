import re


def top_hashtags():
    file = open('in.txt', encoding="utf-8")
    htag_counter = {}
    htag_words = {}
    for line in file.readlines():
        line = line.lower()
        htags = re.findall(r"#\w+", line)
        if not htags:
            continue
        for htag in set(htags):
            if htag in htag_counter:
                htag_counter[htag] += 1
            else:
                htag_counter[htag] = 1
                htag_words[htag] = {}
            for word in line.split():
                '''В ТЗ указано, что "в значащих словах не может быть пробелов и цифр",
                но тут версия слов с дополнительной обрезкой пунктуации.'''
                if re.match(r"[a-zа-я]+\D*", word):
                    word = re.sub(r"[.,!\";:?)\]}']*$", '', word)
                    if word in htag_words[htag]:
                        htag_words[htag][word] += 1
                    else:
                        htag_words[htag][word] = 1
    file.close()
    top10_htags = sorted(htag_counter.items(), key=lambda x: x[1], reverse=True)[:10]
    top10_htags = [tags[0] for tags in top10_htags]
    print(top10_htags)
    top5_words = {}
    for htag in top10_htags:
        top_htag_words = sorted(htag_words[htag].items(), key=lambda x: x[1], reverse=True)[:5]
        top5_words[htag] = [words[0] for words in top_htag_words]
    print(top5_words)


if __name__ == '__main__':
    top_hashtags()
