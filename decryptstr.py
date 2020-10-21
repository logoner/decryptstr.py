"""
Defne Defne
Здравствуйте  . Не поможете ли вы помочь расшифровывать текст начинающему  которая только начала обучает языки программирование.  Вид шифра :шифр простой замены
Данный текст:КЖЛЧШМРЖБНЯЭЪЯПЙЪОЖЩЖВШНЛЖПЖКЯМЯЕЖЩШПЭЫЖПШСЙЦСЯЖЭПРКЖЛЧШМРЗВЯАЙЧЖСЪОЛЭМШВЖЫЖМРЖМЖЯКЛШМРЮЖММЯБНЯЫВЯЫМЯБВЯБМТООЭСШВИЖБЯСВЯБМТШМКПРРНЯЗВРПШЭЙМШЫЖУЫШЮСЯВСЖЮЖМРЖЕПРУШБИРГМЖЭЪЯПЙЪРГЫМЖБРПРЭШЧЯЖЕЯПЙИЖЖЮЖЛЖАНШЛОМЖЫЖПЙЭЯЖЫРМЖММТЖИСШСТВЭСОНЗСМШЪЯМЖЬВВЯБМОСЖЧВЛЖЧЖМЖЧВЪЯЧМШСЖНЛЯЫЯПУШПШЭЙОНЯЛМШЗЛШЕЯСШМШЫЪЯЫЯЧВНЖЛВТГЮРЭПШГДЖВЛШПЗКЛЖБНЛРМЖЭГЯППОЯСЪЛТСТБСЖЪЭСЯЮЖЛЖЫМЯБИРДЛСЖПЖКЛШЧЧТЕЖЛМИСЯЛДДШВЪЯСЯЛЯБРАПШКШПРЭЙНЯЫЛЯЕМЯЭСРЖКЯЕЖЭЖЫТЭВРПЙЭЯМЯЧВЭВЗАРЭАШЗВПЖМРЖЧЯЛШАЛТВЖЫРНПЯЧШСРЮЖЭЪРГЯСМЯИЖМРБЭИШЭКЖЛЧШМРЖБНЯПОЮЖММТЖМЯВТЖАМШЮЖМРЗЪЯЫЯВТГКЛОННЪЯЫШЕТПРРЭНЯПЙАЯВШМТЫПЗЮСЖМРЗИРДЛСЖПЖКЛШЧЧТЬРЧЧЖЛЧШМШВЛЖАОПЙСШСЖДЖВЛШПЗГЯППЭЧЯКНЛЖЫЭСШВРСЙВЧРМРЭСЖЛЭСВЯРМЯЭСЛШММТГЫЖПЖЖЕЯПЖЖНЯПМТБЯСЪЛТСТБСЖЪЭС
 Тема; криптография
 
 My answer:
 re>@Defne Defne
  Here you need to use the frequency analysis of the letters of the Russian language.  See frequency table.
 https://dpva.ru/Guide/GuideUnitsAlphabets/Alphabets/FrequencyRuLetters/
 You take a line of text, count how often different letters are repeated, and based on the table, you make an assumption about the probability of replacement.  You check it with a replacement and if you've guessed right, you get the decrypted text.
"""
#import pprint

#To find a solution, we need
# encrypted message
# dictionary of the frequency of Russian letters

# encrypted message
em = encryptedMessage = "КЖЛЧШМРЖБНЯЭЪЯПЙЪОЖЩЖВШНЛЖПЖКЯМЯЕЖЩШПЭЫЖПШСЙЦСЯЖЭПРКЖЛЧШМРЗВЯАЙЧЖСЪОЛЭМШВЖЫЖМРЖМЖЯКЛШМРЮЖММЯБНЯЫВЯЫМЯБВЯБМТООЭСШВИЖБЯСВЯБМТШМКПРРНЯЗВРПШЭЙМШЫЖУЫШЮСЯВСЖЮЖМРЖЕПРУШБИРГМЖЭЪЯПЙЪРГЫМЖБРПРЭШЧЯЖЕЯПЙИЖЖЮЖЛЖАНШЛОМЖЫЖПЙЭЯЖЫРМЖММТЖИСШСТВЭСОНЗСМШЪЯМЖЬВВЯБМОСЖЧВЛЖЧЖМЖЧВЪЯЧМШСЖНЛЯЫЯПУШПШЭЙОНЯЛМШЗЛШЕЯСШМШЫЪЯЫЯЧВНЖЛВТГЮРЭПШГДЖВЛШПЗКЛЖБНЛРМЖЭГЯППОЯСЪЛТСТБСЖЪЭСЯЮЖЛЖЫМЯБИРДЛСЖПЖКЛШЧЧТЕЖЛМИСЯЛДДШВЪЯСЯЛЯБРАПШКШПРЭЙНЯЫЛЯЕМЯЭСРЖКЯЕЖЭЖЫТЭВРПЙЭЯМЯЧВЭВЗАРЭАШЗВПЖМРЖЧЯЛШАЛТВЖЫРНПЯЧШСРЮЖЭЪРГЯСМЯИЖМРБЭИШЭКЖЛЧШМРЖБНЯПОЮЖММТЖМЯВТЖАМШЮЖМРЗЪЯЫЯВТГКЛОННЪЯЫШЕТПРРЭНЯПЙАЯВШМТЫПЗЮСЖМРЗИРДЛСЖПЖКЛШЧЧТЬРЧЧЖЛЧШМШВЛЖАОПЙСШСЖДЖВЛШПЗГЯППЭЧЯКНЛЖЫЭСШВРСЙВЧРМРЭСЖЛЭСВЯРМЯЭСЛШММТГЫЖПЖЖЕЯПЖЖНЯПМТБЯСЪЛТСТБСЖЪЭС"

# decrypted message
dm = decryptedMessage = ""

# dictionary of the frequency of Russian letters
forl = frequencyOfRussianLetters = {
    "о": 0.10983,
    "е": 0.08483,
    "а": 0.07998,
    "и": 0.07367,
    "н": 0.067,
    "т": 0.06318,
    "с": 0.05473,
    "р": 0.04746,
    "в": 0.04533,
    "л": 0.04343,
    "к": 0.03486,
    "м": 0.03203,
    "д": 0.02977,
    "п": 0.02804,
    "у": 0.02615,
    "я": 0.02001,
    "ы": 0.01898,
    "ь": 0.01735,
    "г": 0.01687,
    "з": 0.01641,
    "б": 0.01592,
    "ч": 0.0145,
    "й": 0.01208,
    "х": 0.00966,
    "ж": 0.0094,
    "ш": 0.00718,
    "ю": 0.00639,
    "ц": 0.00486,
    "щ": 0.00361,
    "э": 0.00331,
    "ф": 0.00267,
    "ъ": 0.00037,
    "ё": 0.00013,
}

# To find out the percentage of the appearance of
# a letter, we must find the total number of
# characters in an encrypted message.

# full percentage (100%)
fullprec = len(em)

#test
#print(fullprec)

#test
#for i in forl:
#    print(i, forl[i])

def printdict(testdict):
    print("{")
    for i in testdict:
        print(i,":",testdict[i])
    print("}")

# Let's calculate the frequency of occurrence of
# letters in an encrypted message

def countLetters(word):
    y = {}
    for i in word:
        if i in y:
            y[i] += 1
        else:
            y[i] = 1
    return y

# dictionary of the frequency of letters in an
# encrypted message
res1 = countLetters(em)

#test
#pprint.pprint(res1)

# Let's transform the dictionary to a convenient form.  
# To do this, we will round the decimal value to
# the fifth character after the floating point.
# (Although we lose a little information about
# accuracy, this is not critical for us.)
res2 = {}

for i in res1:
    #test
    #print(i, round(float(res1[i])/fullprec, 5))
    res2[i] = round(float(res1[i])/fullprec, 5)

# test
#print()

#for i in res2:
#    print(i, res2[i])

#character replacement dictionary
chrepl = {}

# To compile a dictionary of letter replacement, we
# need to find the closest value for the frequency
# of encrypted letters to the frequency of Russian
# letters.  During the comparison process, we need to
# add already established matches to the list.  This
# is necessary to avoid double writing, in the case
# when the frequency coincides with two letters.
# In this case, we will take the first match.

# Основной принцип.
# Сравнить два значения из двух словарей и выбрать самые близкие значения. Сравнивать можно вычитая одно значение из другого и беря модуль результата вычитания. Чем ближе модуль к 0 тем ближе значения.

# Чтобы не выбрать случайно повторно значение из ранее выбранных значений словаря, можно соствить список проверенных значений. И проверять по списку новые значения.

# Сначала объявляем функцию, принимающую два аргумента
# словарь базовый и словарь из закодированного текста.

# Затем создаём список

def transcriptDictionary(basedict, encdict):
    hitlist = [] # лист попаданий для проверенных символов
    resdict = {}
    for baseletter in basedict:
        #print(baseletter, basedict[baseletter])
        minhit = 1.0 # минимальное попадание
        keyhit = "test"
        for encletter in encdict:
            # проверка минимальной разницы
            # получаем разницу
            testhit = abs(basedict[baseletter] - encdict[encletter])
            
            #print(baseletter, abs(basedict(baseletter), encletter, abs(encdict[encletter]), testhit)
            
            # если тестовая разница меньше минимальной
            # которая сохранялась на прошлой итерации
            # присваиваем minhit значение testhit
            if testhit < minhit:
                minhit = testhit 
                keyhit = encletter
        
        #print(keyhit, "=", baseletter)
        
        # записываем в итоговый словарь базовый ключь
        # и ключь из зашифрованного словаря с
        # минимальной разницей.
        # (сюда можно вставить проверку на
        # повторяемость, если было - пропустить шаг)
        if keyhit not in hitlist:
            hitlist.append(keyhit)
        else:
            continue
        
        resdict[baseletter] = keyhit
    
    return resdict

# find offset keys for replacement keys relative to
# the encrypted message
def alphabetical_offset(enckeys):
    ru_alphabet = list("абвгдеёжзийклмнопрстуфхцчшщъыьэюя")
    
    for i in enckeys:
        base = ru_alphabet.index(i)
        encr = ru_alphabet.index(enckeys[i].lower())
        offset = encr - base
        print(i,":",enckeys[i],">>",offset)
        
# decrypting a message using the encryptkeys value and the encrypted message
def decryptingMessage(encrypted_message, encrypted_keys ):
    message = ""
    for i in encrypted_message:
        for key in encrypted_keys:
            if encrypted_keys[key] == i:
                message += key
    return message

# находим ключи замены для шифрования
encryptkeys = transcriptDictionary(forl, res2)

#test
print("пара: буква в обычном алфавите и буква в зашифрованном сообщении")
printdict(encryptkeys)

print()
print("предидущие пары и смещение")
alphabetical_offset(encryptkeys)

dm = decryptingMessage(em, encryptkeys)

print()
print("расшифрованное сообщение (ну почти о_о)")
print()
print(dm)
