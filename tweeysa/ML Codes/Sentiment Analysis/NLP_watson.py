import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, KeywordsOptions

authenticator = IAMAuthenticator('6Hc3iMJs5gGstVanqPXRjaPXmPBO7rhyy4KpSp7USNl4')
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2019-07-12',
    authenticator=authenticator
)

natural_language_understanding.set_service_url('https://api.eu-gb.natural-language-understanding.watson.cloud.ibm.com/instances/b7b78abd-f1ec-4551-89bd-1ba280052302')

response = natural_language_understanding.analyze(
    url='https://twitter.com/kahanikaar_/status/1209402709612232704',
    features=Features(keywords=KeywordsOptions(sentiment=True,emotion=True,limit=2))).get_result()

print(json.dumps(response, indent=2))
