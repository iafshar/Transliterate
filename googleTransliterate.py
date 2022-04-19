
hindiDict = {
    "अ": "a",
    "आ": "aa",
    "ा": "aa",
    "ऊ": "oo",
    "ू": "oo",
    "उ": "u",
    "ु": "u",
    "इ": "i",
    "ि": "i",
    "ई": "ee",
    "ी": "ee",
    "ए": "ey",
    "े": "ey",
    "ऐ": "eh",
    "ै": "eh",
    "ओ": "o",
    "ो": "o",
    "औ": "aw",
    "ौ": "aw",
    "ऍ": "ai",
    "ॅ": "ai",
    "ऑ": "au",
    "ॉ": "au",
    "ऎ": "ai",
    "ॆ": "ai",
    "ऒ": "o",
    "ॊ": "o",
    "ऋ": "ri",
    "ृ": "ri",
    "ॠ": "ree",
    "ॄ": "ree",
    "ऌ": "li",
    "ॢ": "li",
    "ॡ": "lee",
    "ॣ": "lee",
    "्": "",
    "ं": "n",
    "ँ": "n",
    "ः": "h",
    "़": "",
    "क": "ka",
    "ख": "kha",
    "ग": "ga",
    "घ": "gha",
    "च": "cha",
    "छ": "chha",
    "ज": "ja",
    "झ": "jha",
    "ट": "ta",
    "ठ": "tha",
    "ड": "da",
    "ढ": "dha",
    "त": "ta",
    "थ": "tha",
    "द": "da",
    "ध": "dha",
    "न": "na",
    "प": "pa",
    "फ": "pha",
    "ब": "ba",
    "भ": "bha",
    "म": "ma",
    "क़": "qa",
    "ख़": "kha",
    "ग़": "gha",
    "ज़": "za",
    "ड़": "rda",
    "ढ़": "rha",
    "फ़": "fa",
    "य": "ya",
    "र": "ra",
    "ऱ": "rra",
    "ल": "la",
    "ळ": "lla",
    "ऴ": "lla",
    "व": "va",
    "ह": "ha",
    "श": "sha",
    "ष": "sha",
    "स": "sa",
    "ङ": "nga",
    "ञ": "nya",
    "ण": "rna"
}

nuqtaDict = {
    "क": "qa",
    "ख": "kha",
    "ग": "gha",
    "ज": "za",
    "झ": "zha",
    "ड": "rda",
    "ढ": "rha",
    "थ": "tha",
    "फ": "fa",
    "र": "rra",
    "ळ": "lla",
    "ष": "rla"
}

nuqta = "़"

matras = ["ा","ू","ु","ि","ी","े","ै","ो","ौ","ॅ","ॉ","ॆ","ॊ","ृ","ॄ","ॢ","ॣ","्"]
consonants = ["क","ख","ग","घ","च","छ","ज","झ","ट","ठ","ड","ढ","त","थ","द","ध","न","प","फ","ब","भ","म","क़","ख़",
"ग़","ज़","ड़","ढ़","फ़","य","र","ऱ","ल","ळ","ऴ","व","ह","श","ष","स","ङ","ञ","ण"]

transliterated = ""
hindiText = input()
length = len(hindiText)
cutoff = length - 1

for i in range(length):
    current = hindiText[i]

    if i < cutoff:
        next = hindiText[i+1]
    if i > 0:
        previous = hindiText[i-1]

    TransliteratedChar = hindiDict.get(current)
    if TransliteratedChar == None:
        if current == " " and previous in consonants and len(transliterated) > 1:
            transliterated = transliterated[:-1]
        transliterated += current
    else:
        if i > 0 and current in matras and previous in consonants or i > 0 and current in matras and previous == nuqta:
            transliterated = transliterated[:-1]
        elif i < cutoff and next == nuqta:
            nuqtaChar = nuqtaDict.get(current)
            if nuqtaChar != None:
                TransliteratedChar = nuqtaChar
        transliterated += TransliteratedChar

print(transliterated)
