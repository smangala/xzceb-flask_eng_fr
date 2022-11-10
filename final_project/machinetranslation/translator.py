'''Translates French to English and English to French'''
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']


authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english):
    """
    translate english to french
    """
    if english is None:
        return None
    response = language_translator.translate(text=english,model_id="en-fr").get_result()
    french = response['translations'][0]['translation']
    return french

def french_to_english(french):
    """
    translate french to english
    """
    if french is None:
        return None
    response = language_translator.translate(text=french,model_id="fr-en").get_result()
    english = response['translations'][0]['translation']
    return english
