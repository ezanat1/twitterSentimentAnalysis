from textblob import TextBlob
import tweepy
import matplotlib.pyplot as plt

def percentage(part,whole):
    return 100 * float(part)/float(whole)

consumerKey= "XhT1fkX1AVdt3h3mc3lo8VthQ"
consumerSecret = "XzPQ1xw3T0RCOlcxwmVEo5whe7vcJS3mV9tQoyfj79iPznBC85"
accessToken = "534754924-eAnC6UTt8hD1osft5upI94Gjwfp6DBfFIXi1eOnC"
tokenSecret= "b88hxkHsDRF800waHHKZx8oR3wZ9A0FtQ8vQ0U3ZyvRwn"

auth=tweepy.OAuthHandler(consumer_key=consumerKey, consumer_secret=consumerSecret)
auth.set_access_token(accessToken, tokenSecret)
api=tweepy.API(auth)
searchTerm=input('Enter keyword/hastag to search about: ')
numOfSearch=int(input('Enter Number of tweets:'))
tweets = tweepy.Cursor(api.search, q=searchTerm, lang='English').items(numOfSearch)

user = api.me()

print('Name: ' + user.name)
print('Location: ' + user.location)
print('Friends: ' + str(user.friends_count))

'''
positive=0
negative=0
neutral=0
polarity=0

for tweet in tweets:
    analysis = TextBlob(tweet.text)
    polarity += analysis.sentiment.polarity

    if analysis.sentiment.polarity == 0:
        neutral += 1

    elif analysis.sentiment.polarity < 0:
        negative += 1
    elif analysis.sentiment.polarity > 0:
        positive += 1

positive=percentage(positive,numOfSearch)
negative=percentage(negative,numOfSearch)
neutral=percentage(neutral,numOfSearch)
polarity=percentage(polarity,numOfSearch)

positive=format(positive,'.2f')
negative=format(negative,'.2f')
neutral=format(neutral,'.2f')




#print('How people are reacting on'+searchTerm+'by analyzing'+str(searchTerm)+'tweets.')

if polarity==0:
    print('Neutral')
elif polarity < 0.00:
    print('Negative')
elif polarity > 0.00:
    print("Positive")


labels=['Positive ['+str(positive)+'%]', 'Neutral ['+str(neutral)+'%]', 'Negative ['+str(negative)+'%]']
sizes=[positive, neutral, negative]
colors=['yellow','blue','red']
patches, texts = plt.pie(sizes,colors=colors,startangle=90)
plt.legend(patches,labels,loc='best')
plt.title('How people are reacting on '+searchTerm+' by analyzing '+str(searchTerm)+' tweets.')
plt.axis('equal')
plt.tight_layout()
plt.show()





'''


