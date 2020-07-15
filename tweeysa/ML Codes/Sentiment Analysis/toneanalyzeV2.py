import json
from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('QKtodOb0vauIw_xQaFiVb_RUbGP9JMCzriwFqToIUL5Y')
tone_analyzer = ToneAnalyzerV3(
    version='2017-09-21',
    authenticator=authenticator
)

tone_analyzer.set_service_url('https://api.eu-gb.tone-analyzer.watson.cloud.ibm.com/instances/2dcd3376-2e99-4217-8d15-544fa1b1dea7')

import tweepy

#Add your credentials here
twitter_keys = {
        'consumer_key':        'NPOZDKAbob1tBMsDUFQ07gRAr',
        'consumer_secret':     'p0sztMBbhjzUS9ygnZk9ij5yT0lIFeOyxYZKoMBTDhL2M6Vpmy',
        'access_token_key':    '1328561335-ACXCyUvKLz8xKhvBZVy6iyy5H2OS7zjkM2Vtciz',
        'access_token_secret': '2O7CvtFKit2LFrb4h0NhqBf0YKppuWyWmDCukl1yxlDIo'
    }

#Setup access to API
auth = tweepy.OAuthHandler(twitter_keys['consumer_key'], twitter_keys['consumer_secret'])
auth.set_access_token(twitter_keys['access_token_key'], twitter_keys['access_token_secret'])

api = tweepy.API(auth)
text='start '
#Make call on home timeline, print each tweets text
'''public_tweets = api.home_timeline()
for tweet in public_tweets:
    text=text+tweet.text'''

for tweet in tweepy.Cursor(api.search,q="#covid19",count=1,
                           lang="en",
                           since="2020-04-09").items():
    print(tweet.text)
    text=text+tweet.text
    text.rstrip('\n')


print("\n\n\nfinalised string")

text.rstrip('\n')
res=[]

res = " ".join(text.splitlines())
res=res.replace("."," ")
res=res.replace(","," ")
res=res.replace("!"," ")
res=res.replace("?"," ")

print(res)     
tone_analysis = tone_analyzer.tone(
    {'text': res},
    content_type='application/json'
).get_result()
print(json.dumps(tone_analysis, indent=2))
