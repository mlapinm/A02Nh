from googletrans import Translator, constants
from pprint import pprint
# init the Google API translator
# from translate import Translator as Translator2
# translator = Translator()


def translate(text):
    translator = Translator()
    translation = translator.translate(text, src="en", dest="ru")
#     print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")    return translation
    return translation.text

text = "This is a pen."   
# text = '''This chapter '''
translation = translate(text)   
print(translation)
