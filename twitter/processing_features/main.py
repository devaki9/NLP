import csv,json
import emoji
import re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
from nltk.tokenize import word_tokenize
import nltk
from collections import Counter
from nltk.stem import WordNetLemmatizer 
from nltk.corpus import stopwords

def extract_emojis(tweet):

	token_list = word_tokenize(tweet)
	emojis=[]
	for s in token_list:
		if s in emoji.UNICODE_EMOJI :
			emojis.append(s)
	return emojis

def extract_hashtags(tweet):

	tags=[]
	remove = re.compile(r'#')
	for h in re.findall(r'#[\w]+',tweet):
		h=remove.sub('',h)
		tags.append(h)
	return tags

def get_word_count(tweet):

	#count[1] contains count of negative words
	count=[] #count[0] contains count of positive words
	pos=0 
	neg=0
	word_list = re.findall(r'\w+',tweet)
	for word in word_list:
		score = get_sentiment(word)
		if(score > 0.0):
			pos=pos+1
		if(score < 0.0) :
			neg=neg+1
	count.append(pos)
	count.append(neg)
	return count

def get_sentiment(text):
	
	analyzer = SentimentIntensityAnalyzer()
	vs = analyzer.polarity_scores(text)
	score = vs['compound']
	return score

def get_interjection(tweet):
	tweet=tweet.lower()
	count=0
	inter = json.load(open('interjections/interjection.json'))['data']
	wordlist = word_tokenize(tweet)
	for word in wordlist:
		if word in inter:
			count+=1
	return count

def get_intensifier(tweet):
	tweet=tweet.lower()
	count=0
	inten = json.load(open('intensifiers/intensifier.json'))['intensifiers']
	wordlist = word_tokenize(tweet)
	for word in wordlist:
		if word in inten:
			count+=1
	return count

def get_flip(score_tweet,emoji_score):
#positive,negative,neutral
	if( (score_tweet > 0.0 and emoji_score > 0.0) or
			(score_tweet < 0.0 and emoji_score < 0.0) or (score_tweet == 0.0 and emoji_score == 0.0) ):
		return 0
	
	if( (score_tweet == 0.0 and emoji_score != 0.0) or (score_tweet != 0.0 and emoji_score == 0.0) ):
		return 1

	if((score_tweet < 0.0 and emoji_score > 0.0) or (score_tweet > 0.0 and emoji_score < 0.0)):
		return 1


def get_noun_verb(tweet):
	
	pos = []
	tokens = nltk.word_tokenize(tweet.lower())
	tweet = nltk.Text(tokens)
	tags = nltk.pos_tag(tweet)
	counts = Counter(tag for word,tag in tags)
	pos.append(counts['NN'])
	pos.append(counts['VBZ'])
	return pos

def lemmatize_tweet(tweet):
	lemmatizer = WordNetLemmatizer()
	word_list = word_tokenize(tweet)
	result =''
	result = ' '.join([lemmatizer.lemmatize(w) for w in word_list])
	return result

def remove_stopw(tweet):

	result = ''
	result_list=[]
	word_list = word_tokenize(tweet)

	result_list =[word for word in word_list if not word in stopwords.words('english')]
	result = ' '.join(str(e) for e in result_list)
	return result

	
def cleanfile(source,dest):

	#emoji dict
	analyzer = SentimentIntensityAnalyzer()
	contractions_fp = 'contractions/contractions.txt'
	apoDict = json.load(open(contractions_fp))

	file = open(dest, 'w',encoding='UTF-8') 
	ptr = csv.writer(file)
	ptr.writerow(['label','exc_count','quest_count','ellipsis_count','uppercase_count','emoji_score','hashtag_score','tweet_score','positive_word','negative_word','interjection_count','intensifier_count','emoji_tweet_flip','noun_count','verb_count'])

	preprocessed_test = open(dest,'w')
	with open(source,'rt',encoding='utf-8') as file:
		read = csv.reader(file)
		for row in read:
			#remove email-id
			mail = re.compile(r'(\S+@\S+(?:\.\S+)+)')
			tweet = mail.sub('',row[1])

			#remove mentions along with ':'
			remove_mentions = re.compile(r'(?:@[\w]+:)')
			tweet = remove_mentions.sub('',tweet)

			#remove pic.twitter.com/{anything}
			tweet = re.sub(r'pic.twitter.com/[\w]*',"", tweet)

			#remove @ : **Not sure about this
			remove_mentions = re.compile(r'(?:@[\w])')
			tweet = remove_mentions.sub('',tweet)

			#count ellipsis,exclamation,question mark 
			exc_count = tweet.count('!')
			quest_count = tweet.count('?')
			ellipsis_count = tweet.count('...')

			#remove ellipsis,exclamation,question mark
			remove_ellipsis = re.compile(r'[...]')
			tweet = remove_ellipsis.sub('',tweet)

			remove = re.compile(r'[?]')
			tweet = remove.sub('',tweet)

			remove= re.compile(r'[!]')
			tweet = remove.sub('',tweet)

			#uppercase count
			uppercase_count = sum(map(str.isupper, tweet.split()))

			#ADDD EMOTICONS SUPPORT

			#if emoji,then analyse sentiment
			emojis = extract_emojis(tweet)
			emoji_score = get_sentiment(emojis)

			#hashtag sentiment score
			hashtags = extract_hashtags(tweet)
			hashtag_score = get_sentiment(hashtags)

			#handle contractions
			words = tweet.split()
			tweet = [apoDict[word] if word in apoDict else word for word in words]
			tweet = " ".join(tweet)

			#tweet sentiment score(including emoji and #tag?)
			tweet_score = get_sentiment(tweet)

			#remove emojis
			emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  u"\U0001F300-\U0001F5FF"  u"\U0001F680-\U0001F6FF"  
                               u"\U0001F1E0-\U0001F1FF"  
                               u"\U00002500-\U00002BEF"  u"\U00002702-\U000027B0"  u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"  u"\U0001f926-\U0001f937"  u"\U00010000-\U0010ffff"
                               u"\u2640-\u2642"  u"\u2600-\u2B55" u"\u200d" u"\u23cf" u"\u23e9"
                               u"\u231a" u"\ufe0f" u"\u3030"
                               "]+", flags=re.UNICODE)

			tweet = emoji_pattern.sub('',tweet)
			
			#remove '#' AND RETAIN THE HASHTAG TEXT
			remove = re.compile(r'[#]')
			tweet = remove.sub('',tweet)

			#positive word count
			count = []
			count=get_word_count(tweet)
			positive_word=count[0]
			
			#negative word count
			negative_word = count[1]

			#Interjection count 
			interjection_count = get_interjection(tweet)
			
			#intensifier_count
			intensifier_count = get_intensifier(tweet)

			#emoji_tweet_flip(returns 1 if contradiction present else 0)
			score_tweet = get_sentiment(tweet)
			emoji_tweet_flip = get_flip(score_tweet,emoji_score)

			#tweet=tweet.lower()
		
			#Noun_count
			poslist = get_word_count(tweet)
			noun_count = poslist[0]

			#Verb_count
			verb_count = poslist[1]			
			
			#lemmatize
			tweet = lemmatize_tweet(tweet)

			#remove stopwords
			tweet = remove_stopw(tweet)



			ptr.writerow([row[0],exc_count,quest_count,ellipsis_count,uppercase_count,emoji_score,hashtag_score,tweet_score,positive_word,negative_word,interjection_count,intensifier_count,emoji_tweet_flip,noun_count,verb_count
			])			

			





cleanfile('trimmed_test.csv','p_test.csv')
cleanfile('trimmed_train.csv','p_train.csv')


