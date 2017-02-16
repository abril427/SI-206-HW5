import unittest
import tweepy
import requests
import json

## SI 206 - W17 - HW5
## COMMENT WITH:
## Your section day/time: Thurs 6-7
## Any names of people you worked with on this assignment: N/A

######## 500 points total ########

## Write code that uses the tweepy library to search for tweets with a phrase of the user's choice (should use the Python input function), and prints out the Tweet text and the created_at value (note that this will be in GMT time) of the first THREE tweets with at least 1 blank line in between each of them, e.g.

## TEXT: I'm an awesome Python programmer.
## CREATED AT: Sat Feb 11 04:28:19 +0000 2017

## TEXT: Go blue!
## CREATED AT: Sun Feb 12 12::35:19 +0000 2017

## .. plus one more.

## You should cache all of the data from this exercise in a file, and submit the cache file along with your assignment. 

## So, for example, if you submit your assignment files, and you have already searched for tweets about "rock climbing", when we run your code, the code should use CACHED data, and should not need to make any new request to the Twitter API. 
## But if, for instance, you have never searched for "bicycles" before you submitted your final files, then if we enter "bicycles" when we run your code, it _should_ make a request to the Twitter API.

## The lecture notes and exercises from this week will be very helpful for this. 
## Because it is dependent on user input, there are no unit tests for this -- we will run your assignments in a batch to grade them!

## We've provided some starter code below, like what is in the class tweepy examples.

## **** For 50 points of extra credit, create another file called twitter_info.py that contains your consumer_key, consumer_secret, access_token, and access_token_secret, import that file here, and use the process we discuss in class to make that information secure! Do NOT add and commit that file to a public GitHub repository.

## **** If you choose not to do that, we strongly advise using authentication information for an 'extra' Twitter account you make just for this class, and not your personal account, because it's not ideal to share your authentication information for a real account that you use frequently.

## Get your secret values to authenticate to Twitter. You may replace each of these with variables rather than filling in the empty strings if you choose to do the secure way for 50 EC points
consumer_key = "m8Y5EJBzLUB993O53Jron4IKP"
consumer_secret = "P17iHGjTfAJsNDRs6ZJg2w8wNy8BiLSpFPCrLaW3Fe5udPF4Y6"
access_token = "2384595314-tpNOxt9RfqHplfaq0txsDRdwRGhpMl0mG0tKvR5"
access_token_secret = "HC1d6Vp4gbQQVSaCdjxAF58YC4oR5SpC9GFuWuGFma3aJ"
## Set up your authentication to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser()) # Set up library to grab stuff from twitter with your authentication, and return it in a JSON-formatted way

## Write the rest of your code here!

#### Recommended order of tasks: ####
## 1. Set up the caching pattern start -- the dictionary and the try/except statement shown in class.

try:
  twitterFile = open("twitterData.txt", 'r') # Try to read the data from the file
  cache_contents = twitterFile.read() # If it's there, get it into a string
  CACHE_DICTION = json.loads(cache_contents) # And then load it into a dictionary
  twitterFile.close() # Close the file, we're good, we got the data in a dictionary.
except:
  CACHE_DICTION = {} # If there wasn't any data, then the dictionary should be empty. We're gonna rely on this dictionary existing to check if we have any data saved yet. 


## 2. Write a function to get twitter data that works with the caching pattern, so it either gets new data or caches data, depending upon what the input to search for is. You can model this off the class exercise from Tuesday.

def getWithCaching(consumerKey, consumerSecret, accessToken, accessSecret, searchQuery):
  """grab live Twitter data from your user timeline and cache it"""
  if not consumer_secret or not consumer_key:
    print ("You need to fill in client_key and client_secret.")
    exit()

  results_url = api.search(q=searchQuery)

  if searchQuery in CACHE_DICTION: # if we've already made this request
    print('using cache')
      # use stored response
    response_text = CACHE_DICTION[searchQuery] # grab the data from the cache
  else: # otherwise
    print('fetching')
    results = results_url
    CACHE_DICTION[searchQuery] = results   
    # responses = json.dumps(CACHE_DICTION[searchQuery])
    # response_text = responses.text
    # print(response_text)

    #cache data
    twitterFile = open('twitterData.txt', 'w')
    twitterFile.write(json.dumps(CACHE_DICTION))
    twitterFile.close()

    response_text = CACHE_DICTION[searchQuery] # whichver way we got the data, load it into a python object
  return response_text # and return it from the function!


## 3. Invoke your function, save the return value in a variable, and explore the data you got back!

def getTwitterData():
  search_query = input("Please enter your search query: ")
  tweets = getWithCaching(consumer_key, consumer_secret, access_token, access_token_secret, search_query)
  list_of_tweets = tweets["statuses"]
  return list_of_tweets


## 4. With what you learn from the data -- e.g. how exactly to find the text of each tweet in the big nested structure -- write code to print out content from 3 tweets, as shown above.
 
tweets = getTwitterData()
for tweet in (tweets[0:3]):
  print(tweet["text"])
  print(tweet["created_at"])
  print("\n")





