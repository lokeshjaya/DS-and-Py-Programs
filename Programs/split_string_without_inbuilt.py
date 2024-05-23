def split_words(s):
    spl = [" ", ".", ",", ";", ":"]
    words = []
    strr = ""
    for i in s:
        if i in spl:
            if strr:
                words.append(strr)
                strr = ''
        else:
            strr += i
    if strr:
        words.append(strr)


s = "Hello,World"
print(split_words(s))