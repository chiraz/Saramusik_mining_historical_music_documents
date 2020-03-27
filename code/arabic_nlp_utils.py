### Miscellaneous utility functions for preprocessing/cleaning/normalizing Arabic text for NLP purposes.

'''
References:
https://github.com/ahmedaljazzar/arabic-nlp   (Ahmed Jazzar)
https://maximromanov.github.io/2013/01-02.html
https://www.moustaphacheikh.com/2017/11/17/preprocessing  
'''

import re


TATWEEL_UNICODE = '\u0640'

ALIFS_REGEX = re.compile('[إأٱآ]')
HAMZAS_REGEX = re.compile('[ؤئ]')
ALIF_MAKSURA_REGEX = re.compile('ى')
ALIF_MAKSURA_REGEX_2 = re.compile('ى'+'\W')
HA_MARBUTA_REGEX = re.compile('ه'+'\W')
TA_MARBUTA_REGEX = re.compile('ة')
TA_MARBUTA_REGEX_2 = re.compile('ة'+'\W')
TA_MAFTUHA_REGEX = re.compile('ت'+'\W')

STANDARD_LETTERS = u'\u0621\u0622\u0623\u0624\u0625\u0626\u0627\u0628\u0629\u062A\u062B\u062C\u062D\u062E\u062F\u0630\u0631\u0632\u0633\u0634\u0635\u0636\u0637\u0638\u0639\u063A\u0640\u0641\u0642\u0643\u0644\u0645\u0646\u0647\u0648\u0649\u064A'

STANDARD_LETTERS_RANGE = range(ord('\u0621'),ord('\u064A'))  # CAREFUL: THIS INCLUDES TATWIL CHARACTER U+0640
STANDARD_LETTERS_REGEX = re.compile('[' + ''.join([chr(c) for c in STANDARD_LETTERS_RANGE]) + ']')

DIACRITIC_MARKS_RANGE = range(ord('\u064B'),ord('\u0659'))   # Except '\u0654','\u0655'  because they are special hamza marks
DIACRITIC_MARKS_REGEX = re.compile('[' + ''.join([chr(c) for c in DIACRITIC_MARKS_RANGE if c not in ['\u0654','\u0655']]) + ']')


def normalize_arabic_letters(text, remove_tatwil_flag=True, remove_diacritics_flag=True, norm_alif=True, norm_hamza=False, norm_alif_maksura=False, norm_tah_marbuta=False):
    '''Orthographic normalization of common orthographic variations and errors in formal ARabic text.'''

    # replace alef + hamza characters occurring consecutively with a single alef_hamza character (إ or أ).
    text = re.sub(u'\u0627\u0654','أ',text)
    text = re.sub(u'\u0627\u0655','إ',text)

    # replace the non-standard arabic letter 'ٱ'  (\u0671) by a simple alef letter 'ا' (\u0627).
    text = re.sub(u'\u0671','\u0627',text)

    # TO DO: normalize 'ػ', 'ؼ', 'ؽ', 'ؾ', 'ؿ' (U+63b U+63c U+63d U+63e U+63f)
    #   these letters are uncommon in modern formal Arabic text but not sure yet how to handle them.

    if remove_tatwil_flag:
        text = remove_tatwil(text)
    if remove_diacritics_flag:
        text = remove_diacritics(text)
    if norm_alif:
        text = re.sub(ALIFS_REGEX, 'ا', text)    # replace all forms of alef with simple alef
    if norm_hamza:
        text = re.sub(HAMZAS_REGEX, 'ء', text)   # replace all forms of hamza with simple hamza
    if norm_alif_maksura:
        text = re.sub(ALIF_MAKSURA_REGEX, "ي", text)  # replace alef_maksoura with ya   
    if norm_tah_marbuta:
        text = re.sub(TA_MARBUTA_REGEX, "ه", text)    # replace ta marbouta with ha at the end of a word

    return text

def remove_tatwil(text):
    """
    The Tatweel (elongation) is used to stretch words to indicate
    prominence or simply to force vertical justification.
    This symbol has no effect on the meaning of the word so it's
    usually normalized.

    Examples:
        - A word without Tatweel:       جميل
        - The same word with Tatweel:   جـــمـــيـــل
    :param text: The text that we need to extract the Tatweel from.
    :return: A text without Tatweels.
    """
    if text is None:
        return None

    return text.replace(TATWEEL_UNICODE, '')

def remove_diacritics(text):
    return re.sub(DIACRITIC_MARKS_REGEX, '', text)



## UNIT TESTS

if False:
    s = u"\u063a\u064a\u0646\u064a\u0627"   # == 'غينيا'
    print(s)
    print(re.findall(STANDARD_LETTERS_REGEX,s))

if False:
    my_string = ' .'.join(["بِسْمِ اللهِ الرَّحْمٰنِ الرَّحِيمِ" ,  " ؤ ئ إ أ ٱ آ واسى في" , 'جـــمـــيـــل' , "مواڞفات وسعر هاتف أيفون 8  ڞ الجديد"])
    print ("Unit test of normalize_arabic_text_*")
    print("")
    print("Raw text:\n",my_string)
    string2 = re.sub(NON_ARABIC_CHARS_REGEX,' ', my_string)
    print("After replacing non-Arabic letters with space:\n",string2)
    string3 = normalize_arabic_text_1(string2)
    print("After removing tatweel and diacritics:\n",string3)
    string4 = normalize_arabic_text_2(string3)
    print("After orthographic letter normalization:\n",string4)

if False:
    my_string = "مواڞفات وسعر هاتف أيفون 8  ڞ الجديد"
    print(my_string)
    u = re.findall(NON_ARABIC_CHARS_REGEX,my_string)
    print("  contains", len(u), "non-arabic letters.")
    print('  they are:',' '.join(u))

if False:
    my_string = "بِسْمِ اللهِ الرَّحْمٰنِ الرَّحِيمِ"
    print("Before: ",my_string)
    my_string = remove_diacritics(my_string)
    print("After: ",my_string)


