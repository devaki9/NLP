## Essential Packages
```
1.vaderSentiment
2.fasttext
3.pandas
4.numpy
5.sci-kitlearn
6.nltk
7.tweepy
```
## Steps
```
1.Perform Installations as per [Installation.txt](link)
```
```
2.Place Credentials in Credentials.py
```
```
3.Run get_tweet.py.
Tweets are loaded in [realtime_ds.csv]().
```
```
4.Annotate each tweet manually as 1 or 0 in [realtime_ds.csv]().
```
```
5.Run [preprocess_ds.py](). It will generate cleaned_ds.csv.
```
```
6.Run [main_ds.py]().
```



## Project Details

The Goal of this Project is to perform Sarcasm Analysis on data obtained from two Social Media: Twitter and Instagram.
```
1.With the use of official API of Instagram, posts pertaining to hashtags are obtained.
Link to the Instagram API documentation : https://developers.facebook.com/docs/instagram-api/
```
```
2.Twitter offers a robust API along with various libraries for getting data
Tweepy is a library used to work with Twitter API
Link to Tweepy documentation : http://docs.tweepy.org/en/v3.8.0/api.html
```
