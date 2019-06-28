ASCII = 1
DIGIT = 2
ALL = ASCII | DIGIT

# list of ZENKAKU characters
z_ascii = ["ａ", "ｂ", "ｃ", "ｄ", "ｅ", "ｆ", "ｇ", "ｈ", "ｉ",
           "ｊ", "ｋ", "ｌ", "ｍ", "ｎ", "ｏ", "ｐ", "ｑ", "ｒ",
           "ｓ", "ｔ", "ｕ", "ｖ", "ｗ", "ｘ", "ｙ", "ｚ",
           "Ａ", "Ｂ", "Ｃ", "Ｄ", "Ｅ", "Ｆ", "Ｇ", "Ｈ", "Ｉ",
           "Ｊ", "Ｋ", "Ｌ", "Ｍ", "Ｎ", "Ｏ", "Ｐ", "Ｑ", "Ｒ",
           "Ｓ", "Ｔ", "Ｕ", "Ｖ", "Ｗ", "Ｘ", "Ｙ", "Ｚ",
           "！", "”", "＃", "＄", "％", "＆", "’", "（", "）",
           "＊", "＋", "，", "－", "．", "／", "：", "；", "＜",
           "＝", "＞", "？", "＠", "［", "￥", "］", "＾", "＿",
           "‘", "｛", "｜", "｝", "~", "　"]

z_digit = ["０", "１", "２", "３", "４",
       "５", "６", "７", "８", "９"]

# list of HANKAKU characters
h_ascii = ["a", "b", "c", "d", "e", "f", "g", "h", "i",
           "j", "k", "l", "m", "n", "o", "p", "q", "r",
           "s", "t", "", "v", "w", "x", "y", "z",
           "A", "B", "C", "D", "E", "F", "G", "H", "I",
           "J", "K", "L", "M", "N", "O", "P", "Q", "R",
           "S", "T", "", "V", "W", "X", "Y", "Z",
           "!", u'"', "#", "$", "%", "&", "'", "(", ")",
           "*", "+", ",", "-", ".", "/", ":", ";", "<",
           "=", ">", "?", "@", "[", "\\", "]", "^", "_",
           "`", "{", "|", "}", "～", " "]

h_digit = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# maps of ascii
zh_ascii = {}
hz_ascii = {}

for i in range(len(z_ascii)):
    zh_ascii[z_ascii[i]] = h_ascii[i]
    hz_ascii[h_ascii[i]] = z_ascii[i]

del z_ascii, h_ascii

# maps of digit
zh_digit = {}
hz_digit = {}

for i in range(len(z_digit)):
    zh_digit[z_digit[i]] = h_digit[i]
    hz_digit[h_digit[i]] = z_digit[i]

del z_digit, h_digit


#normalize Half-width full-width conversion
def Zen2Han(text="", mode=ALL, ignore=()):
    result = list()

    for c in text:
        if c in ignore:
            result.append(c)

        elif (mode in (1, 3, 5, 7)) and (c in zh_ascii):
            result.append(zh_ascii[c])

        elif (mode in (2, 3, 6, 7)) and (c in zh_digit):
            result.append(zh_digit[c])

        else:
            result.append(c)

    return "".join(result)

def normalize(s):
    s = s.replace('?', '。')
    s = s.replace('？', '。')
    s = s.replace('．', '。')
    
    s = s.replace('，', '、')
    
    s = Zen2Han(s)

    return s